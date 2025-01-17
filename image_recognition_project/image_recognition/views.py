from rest_framework import viewsets
from rest_framework.response import Response
from .models import RecognizedImage
from .serializers import RecognizedImageSerializer
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import numpy as np
from PIL import Image

# Load the ResNet50 model globally (avoids reloading on each request)
model = ResNet50(weights='imagenet')

class RecognizedImageViewSet(viewsets.ModelViewSet):
    queryset = RecognizedImage.objects.all()
    serializer_class = RecognizedImageSerializer

    def create(self, request, *args, **kwargs):
        try:
            # Preprocess the uploaded image
            image_file = request.data['image']
            img = Image.open(image_file).convert('RGB')  # Ensure the image has 3 color channels
            img = img.resize((224, 224))  # ResNet50 expects 224x224 input size
            img_array = np.expand_dims(np.array(img), axis=0)
            img_array = preprocess_input(img_array)  # Preprocess input for ResNet50

            # Perform prediction
            predictions = model.predict(img_array)
            decoded_predictions = decode_predictions(predictions, top=1)[0]
            prediction_label = decoded_predictions[0][1]  # Get the label of the top prediction

            # Save image and prediction
            image_name = default_storage.save('images/' + image_file.name, ContentFile(image_file.read()))
            recognized_image = RecognizedImage.objects.create(image=image_name, prediction=prediction_label)

            # Serialize and return response
            serializer = RecognizedImageSerializer(recognized_image)
            return Response(serializer.data)

        except Exception as e:
            # Handle exceptions gracefully
            return Response({"error": f"An error occurred: {str(e)}"}, status=500)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RecognizedImage

class FeedbackView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            image_name = request.data.get('image_name')
            correct_label = request.data.get('correct_label')

            # Save feedback to the database (or log it)
            RecognizedImage.objects.filter(image=image_name).update(prediction=correct_label)

            return Response({"message": "Feedback submitted successfully."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

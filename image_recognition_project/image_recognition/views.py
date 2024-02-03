from rest_framework import viewsets
from rest_framework.response import Response
from .models import RecognizedImage
from .serializers import RecognizedImageSerializer
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
import numpy as np
from PIL import Image

class RecognizedImageViewSet(viewsets.ModelViewSet):
    queryset = RecognizedImage.objects.all()
    serializer_class = RecognizedImageSerializer

    def create(self, request, *args, **kwargs):
        image_file = request.data['image']
        model = ResNet50(weights='imagenet')

        # Convert the InMemoryUploadedFile to a PIL Image
        img = Image.open(image_file)
        img = img.resize((224, 224))  # Resize the image to the model's expected input size
        img_array = np.expand_dims(np.array(img), axis=0)
        img_array = preprocess_input(img_array)

        # Make predictions
        predictions = model.predict(img_array)
        decoded_predictions = decode_predictions(predictions, top=1)[0]
        prediction_label = decoded_predictions[0][1]

        # Save the image and prediction to the database
        image_name = default_storage.save('images/' + image_file.name, ContentFile(image_file.read()))
        recognized_image = RecognizedImage.objects.create(image=image_name, prediction=prediction_label)

        serializer = RecognizedImageSerializer(recognized_image)
        return Response(serializer.data)

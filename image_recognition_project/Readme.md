# Image Recognition App

This project is an end-to-end application for image recognition, built using **Django** (backend) and **React** (frontend). The backend leverages a pre-trained **ResNet50** model to predict image labels, and the frontend provides a user-friendly interface for uploading images, viewing predictions, and submitting corrections for misclassified images.

## Features

- **Image Upload**: Users can upload images to the server.
- **Image Prediction**: Uses ResNet50 model to predict the label of the uploaded image.
- **Display Uploaded Image**: Uploaded image is displayed along with its prediction.
- **Feedback System**: Users can correct the prediction if it's wrong.

---

## Tech Stack

### Backend:
- **Django**
- **Django REST Framework**
- **TensorFlow** (for ResNet50 model)

### Frontend:
- **React** (using functional components and hooks)
- **Axios** (for API communication)

---

## Installation and Setup

### Prerequisites:
- Python 3.8+
- Node.js 14+
- npm or yarn
- Virtual environment tool (e.g., `venv` or `virtualenv`)

---

### Backend Setup:

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Set up a Python virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate  # For Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run database migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

---

### Frontend Setup:

1. Navigate to the `image-recognition-frontend` folder:
    ```bash
    cd image-recognition-frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Start the React development server:
    ```bash
    npm start
    ```

---

## Usage

1. Access the application:
   - Backend API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Frontend: [http://localhost:3000](http://localhost:3000)

2. **Upload an Image**:
   - Use the file upload button to select an image.
   - Click on "Upload" to send the image to the backend for prediction.

3. **View Prediction**:
   - After the upload, the app displays the uploaded image and its predicted label.

4. **Correct the Prediction**:
   - If the prediction is incorrect, enter the correct label and submit it.
   - The correction is saved in the backend for future improvements.

---

## File Structure

### Backend:
- `image_recognition_project/`
  - `settings.py`: Django project settings.
  - `urls.py`: URL configurations.
  - `views.py`: API views for image recognition and feedback.
  - `models.py`: Database models for storing images and predictions.

### Frontend:
- `image-recognition-frontend/`
  - `src/`
    - `App.js`: Main React component.
    - `api/`: Axios API configuration.
    - `components/`: Reusable React components.

---

## API Endpoints

### 1. Recognized Images:
- **Endpoint**: `/api/recognized-images/`
- **Method**: `POST`
- **Description**: Accepts an image file and returns the predicted label.

### 2. Feedback:
- **Endpoint**: `/api/feedback/`
- **Method**: `POST`
- **Description**: Accepts corrections for predicted labels.

---

## Troubleshooting

### Common Issues:

1. **`ModuleNotFoundError: No module named 'tensorflow'`:**
   - Ensure TensorFlow is installed with the correct version: `pip install tensorflow`.

2. **CORS Issues:**
   - Configure Django CORS headers in `settings.py`:
     ```python
     INSTALLED_APPS += ['corsheaders']
     MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE
     CORS_ALLOW_ALL_ORIGINS = True  # For development only
     ```

3. **Frontend Errors (e.g., `web-vitals`):**
   - Ensure all dependencies are installed: `npm install web-vitals`

---

## Future Enhancements

- Implement user authentication.
- Allow batch uploads for multiple image predictions.
- Store and display prediction history for users.
- Integrate a more advanced model (e.g., InceptionV3).

---

## License

 

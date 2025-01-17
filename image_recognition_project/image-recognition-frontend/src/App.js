import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [preview, setPreview] = useState(null);
    const [prediction, setPrediction] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [correctionMode, setCorrectionMode] = useState(false);
    const [correctLabel, setCorrectLabel] = useState('');

    // Handle file selection
    const handleFileChange = (event) => {
        const file = event.target.files[0];
        setSelectedFile(file);
        setPrediction('');
        setError('');
        setCorrectionMode(false);

        // Generate a preview URL for the selected file
        if (file) {
            const previewUrl = URL.createObjectURL(file);
            setPreview(previewUrl);
        } else {
            setPreview(null);
        }
    };

    // Handle file upload
    const handleFileUpload = async (event) => {
        event.preventDefault();

        if (!selectedFile) {
            setError('Please select an image file.');
            return;
        }

        const formData = new FormData();
        formData.append('image', selectedFile);

        try {
            setLoading(true);
            setError('');
            const response = await axios.post('http://127.0.0.1:8000/api/recognized-images/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            setPrediction(response.data.prediction); // Update with the prediction from the backend
        } catch (err) {
            setError('An error occurred while processing the image.');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    // Handle correction submission
    const handleCorrectionSubmit = async () => {
        if (!correctLabel.trim()) {
            setError('Please enter a valid label.');
            return;
        }

        try {
            setLoading(true);
            const response = await axios.post('http://127.0.0.1:8000/api/feedback/', {
                image_name: selectedFile.name,
                correct_label: correctLabel,
            });

            setCorrectionMode(false);
            setCorrectLabel('');
            alert('Thank you for your feedback!');
        } catch (err) {
            setError('An error occurred while submitting the correction.');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ maxWidth: '500px', margin: '50px auto', textAlign: 'center' }}>
            <h1>Image Recognition</h1>
            <form onSubmit={handleFileUpload}>
                <input type="file" accept="image/*" onChange={handleFileChange} />
                <button type="submit" disabled={loading} style={{ marginLeft: '10px' }}>
                    {loading ? 'Uploading...' : 'Upload'}
                </button>
            </form>

            {error && <p style={{ color: 'red' }}>{error}</p>}

            {/* Show uploaded image preview */}
            {preview && (
                <div style={{ marginTop: '20px' }}>
                    <h3>Uploaded Image:</h3>
                    <img
                        src={preview}
                        alt="Uploaded Preview"
                        style={{ maxWidth: '100%', height: 'auto', border: '1px solid #ddd', borderRadius: '5px' }}
                    />
                </div>
            )}

            {/* Show prediction result */}
            {prediction && (
                <div style={{ marginTop: '20px' }}>
                    <h3>Prediction:</h3>
                    <p style={{ fontWeight: 'bold', fontSize: '18px' }}>{prediction}</p>
                    {!correctionMode && (
                        <button onClick={() => setCorrectionMode(true)} style={{ marginTop: '10px' }}>
                            Correct Prediction
                        </button>
                    )}
                </div>
            )}

            {/* Correction mode */}
            {correctionMode && (
                <div style={{ marginTop: '20px' }}>
                    <h3>Enter Correct Label:</h3>
                    <input
                        type="text"
                        value={correctLabel}
                        onChange={(e) => setCorrectLabel(e.target.value)}
                        placeholder="Correct label"
                        style={{ marginRight: '10px' }}
                    />
                    <button onClick={handleCorrectionSubmit} disabled={loading}>
                        Submit
                    </button>
                </div>
            )}
        </div>
    );
}

export default App;

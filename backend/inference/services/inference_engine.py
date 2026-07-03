from pathlib import Path

import cv2
import numpy as np
import onnxruntime as ort


class InferenceEngine:
    """
    Loads the ONNX model and provides methods for
    retrieving model information and running inference.
    """

    def __init__(self):
        # Project root
        self.project_root = Path(__file__).resolve().parents[3]

        # Models directory
        self.models_dir = self.project_root / "models"

        # ONNX model path
        self.model_path = self.models_dir / "convnextv2.onnx"

        # Check if model exists
        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Model not found:\n{self.model_path}"
            )

        # Load ONNX model
        self.session = ort.InferenceSession(
            str(self.model_path),
            providers=["CPUExecutionProvider"]
        )

        self.class_names = [
            "buildings",
            "forest",
            "glacier",
            "mountain",
            "sea",
            "street",
        ]

    def get_model_info(self):
        """
        Return basic information about the loaded model.
        """
        return {
            "model_name": self.model_path.name,
            "providers": self.session.get_providers(),
            "inputs": [
                inp.name for inp in self.session.get_inputs()
            ],
            "outputs": [
                out.name for out in self.session.get_outputs()
            ]
        }
    
    def preprocess(self, image):
        """
        Preprocess an OpenCV image for ConvNeXt inference.
        """

        image = cv2.resize(image, (224, 224))

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image = image.astype(np.float32) / 255.0

        mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
        std = np.array([0.229, 0.224, 0.225], dtype=np.float32)

        image = (image - mean) / std

        image = np.transpose(image, (2, 0, 1))

        image = np.expand_dims(image, axis=0)

        return image.astype(np.float32)
    

    def predict(self, image):
        """
        Run inference on an OpenCV image and return
        the predicted class and confidence score.
        """

        # Preprocess image
        input_tensor = self.preprocess(image)

        # Get input and output names
        input_name = self.session.get_inputs()[0].name
        output_name = self.session.get_outputs()[0].name

        # Run inference
        logits = self.session.run(
            [output_name],
            {input_name: input_tensor}
        )[0]

        logits = logits.squeeze()

        # Softmax
        exp = np.exp(logits - np.max(logits))
        probabilities = exp / np.sum(exp)

        # Prediction
        class_index = np.argmax(probabilities)

        prediction = self.class_names[class_index]
        confidence = float(probabilities[class_index])

        return {
            "prediction": prediction,
            "confidence": round(confidence * 100, 2)
        }
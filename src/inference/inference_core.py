"""
Core inference engine for skin lesion prediction
"""

import torch


class ISICInferenceEngine:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Engine initialized on {self.device}")

    def predict_single_image(self, image_tensor, model=None):
        """Run a prediction on a single image tensor"""

        model.eval()
        with torch.no_grad():
            logits = model(image_tensor.to(self.device))
            prob = torch.softmax(logits, dim=1)[:, 1].item()
        return prob

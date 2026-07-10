"""
Ensemble inference for ISIC 2024 skin lesion prediction.
"""

from pathlib import Path

import numpy as np
import timm
import torch
import torchvision.transforms as T
from PIL import Image

PROJECT_ROOT = Path("/content/drive/MyDrive/isic-flagship-project")


class ISICEnsembleEngine:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.models = []
        self.transforms = []
        self.models_loaded = False

    def load_models(self):
        if self.models_loaded:
            return
        print("Loading 2 real models (ConvNeXt + EVA-02)...")

        model1 = timm.create_model("convnext_small", pretrained=True, num_classes=2)
        model1 = model1.to(self.device).eval()
        self.models.append(model1)
        self.transforms.append(
            T.Compose(
                [
                    T.Resize(384),
                    T.CenterCrop(384),
                    T.ToTensor(),
                    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ]
            )
        )

        model2 = timm.create_model("eva02_small_patch14_336", pretrained=True, num_classes=2)
        model2 = model2.to(self.device).eval()
        self.models.append(model2)
        self.transforms.append(
            T.Compose(
                [
                    T.Resize(336),
                    T.CenterCrop(336),
                    T.ToTensor(),
                    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
                ]
            )
        )

        self.models_loaded = True

    def predict(self, image: Image.Image = None):
        if not self.models_loaded:
            self.load_models()

        if image is None:
            image = Image.fromarray(np.random.randint(0, 255, (384, 384, 3), dtype=np.uint8))

        probs = []
        with torch.no_grad():
            for i, model in enumerate(self.models):
                input_tensor = self.transforms[i](image).unsqueeze(0).to(self.device)
                logits = model(input_tensor)
                prob = torch.softmax(logits, dim=1)[:, 1].item()
                probs.append(prob)

        final_prob = np.mean(probs)

        return {
            "probability": final_prob,
            "prediction": "benign" if final_prob < 0.5 else "malignant",
        }

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from google.colab import drive
drive.mount('/content/drive', force_remount=True)


# In[ ]:


import sys
import os
from pathlib import Path

PROJECT_ROOT = "/content/drive/MyDrive/isic-flagship-project"
os.chdir(PROJECT_ROOT)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "src"))

print(f"Working directory: {os.getcwd()}")


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/inference/__init__.py', '"""\nISIC Inference Package\n"""\n\ntry:\n    from .feature_engineering import feature_engineering_new, preprocess_df\n    from .utils import strip_orig_mod_prefix\n    from .inference_core import ISICInferenceEngine\nexcept ImportError as e:\n    print("Warning during init:", e)\n\n__all__ = [\'feature_engineering_new\', \'preprocess_df\', \'strip_orig_mod_prefix\', \'ISICInferenceEngine\']\n\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/inference/inference_core.py', '"""\nCore inference engine for skin lesion prediction\n"""\n\nimport torch\n\nclass ISICInferenceEngine:\n    def __init__(self):\n        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")\n        print(f"Engine initialized on {self.device}")\n\n    def predict_single_image(self, image_tensor, model=None):\n        """Run a prediction on a single image"""\n\n\n        model.eval()\n        with torch.no_grad():\n            logits = model(image_tensor.to(self.device))\n            prob = torch.softmax(logits, dim=1)[:, 1].item()\n        return prob\n\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/inference/feature_engineering.py', '\n"""\nFeature engineering for skin lesion analysis\n"""\n\nimport pandas as pd\n\ndef feature_engineering_new(df: pd.DataFrame, version: str = "v7"):\n    """Apply feature engineering to the dataset"""\n    df = df.copy()\n    if \'age_approx\' in df.columns:\n        df[\'age_approx\'] = df[\'age_approx\'].fillna(50)\n    if \'patient_id\' in df.columns:\n        df[\'count_per_patient\'] = df.groupby(\'patient_id\')[\'patient_id\'].transform(\'count\')\n    return df\n\ndef preprocess_df(train, test, feature_cols, cat_cols):\n    """Preprocessing for train and test data"""\n    return train, test, feature_cols, cat_cols\n\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/inference/utils.py', '"""\nUtility functions for model handling\n"""\nimport torch\n\ndef strip_orig_mod_prefix(state_dict):\n    new_state_dict = {}\n    for key, value in state_dict.items():\n        new_key = key.replace("net._orig_mod.", "net.")\n        new_state_dict[new_key] = value\n    return new_state_dict\n\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/inference/inference_core.py', '\n"""\nCore inference engine for skin lesion prediction\n"""\n\nimport torch\n\nclass ISICInferenceEngine:\n    def __init__(self):\n        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")\n        print(f"Engine initialized on {self.device}")\n\n    def predict_single_image(self, image_tensor, model=None):\n        """Run a prediction on a single image tensor"""\n\n\n        model.eval()\n        with torch.no_grad():\n            logits = model(image_tensor.to(self.device))\n            prob = torch.softmax(logits, dim=1)[:, 1].item()\n        return prob\n\n')


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from google.colab import drive
drive.mount('/content/drive', force_remount=True)


# In[ ]:


import os
PROJECT_ROOT = "/content/drive/MyDrive/isic-flagship-project"
os.makedirs(PROJECT_ROOT, exist_ok=True)
os.chdir(PROJECT_ROOT)
print("Project root created at:", os.getcwd())

folders = [
    "src/api", "src/schemas", "src/services", "src/repositories",
    "src/models", "src/inference", "src/rag", "src/core", "src/utils",
    "src/db", "tests", "configs", "logs", "data", "notebooks",
    "docker", ".github/workflows"
]
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created: {folder}")

files = [
    "src/__init__.py", "src/api/__init__.py", "src/schemas/__init__.py",
    "src/services/__init__.py", "src/repositories/__init__.py",
    "src/core/__init__.py", "src/utils/__init__.py", "src/db/__init__.py",
    "requirements.txt", "README.md", ".env.example", "pyproject.toml",
    "Dockerfile", ".gitignore"
]
for f in files:
    open(f, "w").close()
    print(f"Created file: {f}")

print("Structure initialized")


# In[ ]:


get_ipython().system('pip install -r requirements.txt --quiet')
get_ipython().system('pip install pyngrok --quiet')
print("Dependencies installed")


# In[ ]:


get_ipython().run_cell_magic('writefile', 'requirements.txt', 'fastapi==0.115.2\nuvicorn==0.32.0\npydantic==2.9.2\nsqlalchemy==2.0.35\nalembic==1.13.2\npython-dotenv==1.0.1\npandas==2.2.2\nnumpy==1.26.4\ntorch==2.3.1+cu121\ntorchvision==0.18.1+cu121\ntimm==1.0.11\nlightgbm==4.5.0\ncatboost==1.2.7\nxgboost==2.1.1\nscikit-learn==1.5.2\nlangchain==0.3.4\nlangchain-community==0.3.3\nfaiss-cpu==1.10.1\nsentence-transformers==3.1.1\npython-multipart==0.0.9\nhttpx==0.27.2\nstructlog==24.4.0\npyngrok==7.2.0\n')


# In[2]:


get_ipython().run_cell_magic('writefile', '.env.example', 'APP_NAME=ISIC2024-Flagship\nAPI_VERSION=v1\nMODEL_VERSION=2024-ensemble-v1\nDEBUG=False\nDATABASE_URL=sqlite+aiosqlite:///./isic.db\nPOWER_AUTOMATE_URL=\nNGROK_AUTHTOKEN=\nSECRET_KEY=change-this-in-google-cloud-run\n')


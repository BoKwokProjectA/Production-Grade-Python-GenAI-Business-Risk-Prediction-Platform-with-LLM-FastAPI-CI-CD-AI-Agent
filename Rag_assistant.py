#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from google.colab import drive
drive.mount('/content/drive', force_remount=True)


# In[ ]:


import sys
import os

PROJECT_ROOT = "/content/drive/MyDrive/isic-flagship-project"
os.chdir(PROJECT_ROOT)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "src"))

get_ipython().system('pip install langchain langchain-community langchain-openai faiss-cpu sentence-transformers -q')

print(f"Working directory: {os.getcwd()}")


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/rag/rag_engine.py', '"""\nRAG engine for answering questions about the project\n"""\n\nimport glob\nfrom langchain_community.vectorstores import FAISS\nfrom langchain_community.embeddings import HuggingFaceEmbeddings\nfrom langchain_text_splitters import RecursiveCharacterTextSplitter\n\nclass RAGEngine:\n    def __init__(self):\n        self.embeddings = HuggingFaceEmbeddings(\n            model_name="sentence-transformers/all-MiniLM-L6-v2"\n        )\n        self.vectorstore = None\n\n    def index_project(self):\n        documents = []\n\n\n        for filepath in glob.glob("src/**/*.py", recursive=True):\n            try:\n                with open(filepath, "r", encoding="utf-8") as f:\n                    content = f.read()\n                    documents.append(f"File: {filepath}\\n{content[:2000]}")\n            except:\n                pass\n\n        documents.append("""\n        This project implements a skin lesion analysis system based on the\n        1st and 2nd place solution from ISIC 2024 competition.\n        It includes an ensemble of vision models, GBDT blending,\n        and a FastAPI backend.\n        """)\n\n        text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)\n        texts = text_splitter.create_documents(documents)\n\n        self.vectorstore = FAISS.from_documents(texts, self.embeddings)\n        print(f"Indexed {len(texts)} document chunks")\n        return self.vectorstore\n\n    def ask(self, question: str):\n        if self.vectorstore is None:\n            self.index_project()\n\n        docs = self.vectorstore.similarity_search(question, k=3)\n        context = "\\n\\n".join([doc.page_content[:400] for doc in docs])\n\n        return f"""Context from project:\\n{context[:600]}...\\n\\nQuestion: {question}"""\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/api/rag_routes.py', '"""\nRoutes of RAG Assistant\n"""\n\nfrom fastapi import APIRouter\nfrom pydantic import BaseModel\nfrom src.rag.rag_engine import RAGEngine\n\nrag_router = APIRouter()\nrag_engine = RAGEngine()\n\nclass ChatRequest(BaseModel):\n    question: str\n\nclass ChatResponse(BaseModel):\n    answer: str\n\n@rag_router.post("/chat", response_model=ChatResponse)\nasync def chat_with_assistant(request: ChatRequest):\n    """Chat with the RAG assistant"""\n    answer = rag_engine.ask(request.question)\n    return ChatResponse(answer=answer)\n\n')


# In[ ]:


get_ipython().run_cell_magic('writefile', '/content/drive/MyDrive/isic-flagship-project/src/api/main.py', '"""\nMain FastAPI application\n"""\n\nfrom fastapi import FastAPI\nfrom fastapi.middleware.cors import CORSMiddleware\n\nfrom src.core.config import get_settings\nfrom src.api.routes import health_router, prediction_router\nfrom src.api.rag_routes import rag_router\n\nsettings = get_settings()\n\napp = FastAPI(\n    title=settings.APP_NAME,\n    version=settings.API_VERSION,\n    description="ISIC 2024 Skin Cancer Detection API"\n)\n\napp.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])\n\napp.include_router(health_router, prefix="/api/v1", tags=["health"])\napp.include_router(prediction_router, prefix="/api/v1", tags=["prediction"])\napp.include_router(rag_router, prefix="/api/v1", tags=["rag"])   # ← Added\n\n@app.get("/")\nasync def root():\n    return {"message": "ISIC 2024 Flagship API is running"}\n')


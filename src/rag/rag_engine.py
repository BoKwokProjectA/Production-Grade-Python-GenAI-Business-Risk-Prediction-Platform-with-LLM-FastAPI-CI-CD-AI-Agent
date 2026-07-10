"""
RAG engine for answering questions about the project
"""

import glob

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter


class RAGEngine:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vectorstore = None

    def index_project(self):
        documents = []

        for filepath in glob.glob("src/**/*.py", recursive=True):
            try:
                with open(filepath, encoding="utf-8") as f:
                    content = f.read()
                    documents.append(f"File: {filepath}\n{content[:2000]}")
            except Exception as exc:
                print(f"Skipping {filepath}: {exc}")

        documents.append("""
        This project implements a skin lesion analysis system based on the
        1st and 2nd place solution from ISIC 2024 competition.
        It includes an ensemble of vision models, GBDT blending,
        and a FastAPI backend.
        """)

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
        texts = text_splitter.create_documents(documents)

        self.vectorstore = FAISS.from_documents(texts, self.embeddings)
        print(f"Indexed {len(texts)} document chunks")
        return self.vectorstore

    def ask(self, question: str):
        if self.vectorstore is None:
            self.index_project()

        docs = self.vectorstore.similarity_search(question, k=3)
        context = "\n\n".join([doc.page_content[:400] for doc in docs])

        return f"""Context from project:\n{context[:600]}...\n\nQuestion: {question}"""

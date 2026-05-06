from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# -------------------------------
# LOAD TEXT DATA (FAQ / EXPLANATIONS)
# -------------------------------
loader = TextLoader("data/students.txt")
documents = loader.load()

print("Loaded Data:", documents)

# -------------------------------
# SPLIT TEXT
# -------------------------------
splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

docs = splitter.split_documents(documents)

print("Chunks:", docs)

# -------------------------------
# EMBEDDINGS MODEL
# -------------------------------
embeddings = HuggingFaceEmbeddings()

# -------------------------------
# CREATE FAISS INDEX
# -------------------------------
db = FAISS.from_documents(docs, embeddings)

# -------------------------------
# SAVE VECTOR DB
# -------------------------------
db.save_local("faiss_index")

print("Vector DB Created Successfully!")
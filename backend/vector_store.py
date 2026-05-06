from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Load data
loader = TextLoader("data/students.txt")
documents = loader.load()

print("Loaded Data:", documents)

# Split data
splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
docs = splitter.split_documents(documents)

print("Chunks:", docs)

# Convert to embeddings
embeddings = HuggingFaceEmbeddings()

# Store in FAISS
db = FAISS.from_documents(docs, embeddings)
db.save_local("faiss_index")

print("Vector DB Created Successfully!")
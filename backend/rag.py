from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from langchain.prompts import PromptTemplate

# ---------------- LLM ----------------
pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=200,
    do_sample=False
)

llm = HuggingFacePipeline(pipeline=pipe)

# ---------------- EMBEDDINGS ----------------
embeddings = HuggingFaceEmbeddings()

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# ---------------- PROMPT ----------------
rag_prompt = PromptTemplate(
    template="""
You are a student AI assistant.

Use the context to answer accurately.

Context:
{context}

Question:
{question}

Answer in simple format.
""",
    input_variables=["context", "question"]
)

# ---------------- CHAIN ----------------
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
    chain_type="stuff",
    chain_type_kwargs={"prompt": rag_prompt}
)

def run_rag(query: str):
    return qa_chain.run(query)
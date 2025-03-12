import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pconeclient import pc
# from aimodel import model

index_name = "document-search"
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Chunk the document
def chunk_text(text, chunk_size=500, chunk_overlap=100):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    return text_splitter.split_text(text)

# Convert to embeddings and store in Pinecone
def store_embeddings(text_chunks):
    index = pc.Index(index_name)  # Connect to the Pinecone index
    embeddings = model.encode(text_chunks)  # Convert to embeddings

    # Store in Pinecone
    for i, (chunk, embedding) in enumerate(zip(text_chunks, embeddings)):
        index.upsert(vectors=[(str(i), embedding.tolist(), {"chunk": chunk})])

    print("Embeddings stored successfully!")
    return index

# Load PDF, chunk text, generate embeddings, and store
pdf_text = extract_text_from_pdf("/content/financial aid course.pdf")
chunks = chunk_text(pdf_text)
index = store_embeddings(chunks)
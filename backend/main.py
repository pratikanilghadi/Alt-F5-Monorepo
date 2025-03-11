from fastapi import FastAPI, UploadFile, HTTPException
from model import EmbeddingData, SearchQuery
from dependencies.embeddings import embed
from dependencies.embeddings import pinesearch

import os

app = FastAPI()

@app.get("/")
def default_route() -> dict[str,str]:
    return {"message":"Server Up and Running"}

#Todo : Pending Routes to build
# Convert the document files to embeddings (username, file/filepath)
# Provide the document ids based on the query (username, query)

@app.post("/doc-parse")
def document_processor(user_id:str, file:UploadFile) -> dict[str,str]:
    _, file_extension = os.path.splitext(file.filename)
    file_extension = file_extension.lower()
    
    # Validate the file extension
    if file_extension not in ['.pdf']:
        raise HTTPException(
            status_code=400, 
            detail=f"Unsupported file type: {file_extension}. Only PDF files are supported."
        )
    
    file_content = file.file.read()

    if embed(user_id=user_id, file_content=file_content):
        return {"message":"file has been successfully embedded"}
    else:
        return {"message":"file has not been processed due to server issue"}

@app.post("/search_query")
def query_search(user_id:str, query:str) -> dict[str,str]:
    document_ids, chunk_ids = pinesearch(user_id=user_id, query=query)
    return {
        "document_ids":document_ids,
        "chunk_ids":chunk_ids
    }
from fastapi import FastAPI, UploadFile, HTTPException
from model import EmbeddingData, SearchQuery
from dependencies.embeddings import embed

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
    
    
    
    return {"message": f"Successfully validated {file.filename}", "file_type": file_extension[1:]}

@app.post("/search_query")
def query_search(params: SearchQuery) -> dict[str,str]:
    return {"message":"route is functional"}
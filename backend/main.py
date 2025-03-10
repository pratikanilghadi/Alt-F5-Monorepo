from fastapi import FastAPI
from model import EmbeddingData, SearchQuery
app = FastAPI()

@app.get("/")
def default_route() -> dict[str,str]:
    return {"message":"Server Up and Running"}

#Todo : Pending Routes to build
# Convert the document files to embeddings (username, file/filepath)
# Provide the document ids based on the query (username, query)

@app.post("/doc-parse")
def document_processor(params: EmbeddingData) -> dict[str,str]:
    return {"message":"route is functional"}

@app.post("/search_query")
def query_search(params: SearchQuery) -> dict[str,str]:
    return {"message":"route is functional"}
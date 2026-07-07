from pydantic import BaseModel
from datetime import datetime


class documentUploadResponse(BaseModel):

    id: int
    filename: str
    created_at: datetime
    chunk_count: int

    model_config={"from attributes":True}


class DocumentOut(BaseModel):
    id: int
    filename: str
    created_at : datetime

    model_config={"from attributes":True}

class ChunkOut(BaseModel):
    id : int
    document_id : int
    chunk_index : int
    content: str

    model_config={"from attributes":True}

    

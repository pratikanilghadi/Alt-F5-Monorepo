from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import List, Optional
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def _get_validators_(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def _modify_schema_(cls, field_schema):
        field_schema.update(type="string")


class UserSchema(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str}
        arbitrary_types_allowed = True


class DocumentSchema(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    user_id: PyObjectId
    filename: str
    file_type: str
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str}
        arbitrary_types_allowed = True

class ChunkSchema(BaseModel): 
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    document_id: PyObjectId
    text: str
    embedding: List[float]
    metadata: dict

    class Config:
        json_encoders = {ObjectId: str}
        arbitrary_type_allowed = True

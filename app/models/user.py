from pydantic import BaseModel, EmailStr
from typing import Optional
from bson import ObjectId

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str

class User(UserBase):
    id: str
    is_active: bool = True

    # Add this method to handle MongoDB document conversion
    @classmethod
    def from_mongo(cls, mongo_doc):
        if mongo_doc:
            mongo_doc["id"] = str(mongo_doc.pop("_id"))
            return cls(**mongo_doc)
        return None
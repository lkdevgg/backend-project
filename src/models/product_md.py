from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import datetime
from .PyObjectId import PyObjectId


class ProductModel(BaseModel):
    name: str = Field(
        None, title="Product Name", max_length=500
    )
    price: float = Field(..., gt=0,
                         description="The price must be greater than zero")
    created_by: EmailStr = Field(
        None, title="Creater Email"
    )

    def as_dict(self):
        return {"name": self.name,
                "price": self.price,
                "created_by": self.created_by,
                "created_at": datetime.datetime.now()}


class ProductUpdateModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(
        None, title="Product Name", max_length=500
    )
    price: float = Field(..., gt=0,
                         description="The price must be greater than zero")
    updated_by: Optional[EmailStr] = Field(
        None, title="Updater Email"
    )

    def as_dict(self):
        return {"id": self.id,
                "name": self.name,
                "price": self.price,
                "updated_at": datetime.datetime.now(),
                "updated_by": self.updated_by}


def ResponseModel(data, code, message, error):
    return {
        "data": [data],
        "code": code,
        "message": message,
        "error": error
    }

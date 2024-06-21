# from typing import List, Optional, Generic, TypeVar
# from pydantic import BaseModel, Field
# import numpy as np

# # Define the PyVector class
# class PyVector:
#     def __init__(self, elements: List[float]):
#         self.elements = np.array(elements)

#     def __repr__(self):
#         return f"PyVector({self.elements.tolist()})"

# T = TypeVar('T')

# # Define the Pydantic models
# class BookSchema(BaseModel):
    
#     id: Optional[int] = None
#     title: Optional[str] = None
#     description: Optional[str] = None
#     vector: Optional[PyVector] = None  # Adding PyVector field

#     class Config:
#         from_attributes = True  # Updated from `orm_mode` to `from_attributes`
#         arbitrary_types_allowed = True  # Allow arbitrary types

# class Request(BaseModel, Generic[T]):
#     parameter: Optional[T] = Field(...)

# class RequestBook(BaseModel):
#     parameter: BookSchema = Field(...)

# class Response(BaseModel, Generic[T]):
#     code: str
#     status: str
#     message: str
#     result: Optional[T]

# # Example usage
# book = BookSchema(
#     id=1,
#     title="Example Book",
#     description="This is an example book",
#     vector=PyVector([1.0, 2.0, 3.0])
# )
# print(book)
# schemas.py
from typing import List, Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    list: List[str]

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

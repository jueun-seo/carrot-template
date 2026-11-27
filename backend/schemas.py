from datetime import datetime
from pydantic import BaseModel, Field


class UserOut(BaseModel):
  id: int
  username: str


class UserCreate(BaseModel):
  username: str = Field(min_length=3, max_length=20)
  password: str = Field(min_length=4)


class Token(BaseModel):
  access_token: str
  token_type: str


class ImageOut(BaseModel):
  id: int
  image_url: str


class ProductOut(BaseModel):
  id: int
  title: str
  price: int
  description: str
  shipping_fee: int | None
  meeting_place: str | None
  status: str
  seller_id: int
  created_at: datetime
  images: list[ImageOut]

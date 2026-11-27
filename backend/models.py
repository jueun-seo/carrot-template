from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class User(Base):
  __tablename__ = 'users'

  id: Mapped[int] = mapped_column(primary_key=True)
  username: Mapped[str] = mapped_column(unique=True)
  password_hash: Mapped[str]


class RefreshToken(Base):
  __tablename__ = 'refresh_tokens'

  # 토큰마다 고유 번호(jti)
  id: Mapped[str] = mapped_column(primary_key=True)
  user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))


class Product(Base):
  __tablename__ = 'products'

  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str]
  price: Mapped[int]
  description: Mapped[str]
  shipping_fee: Mapped[int | None]
  meeting_place: Mapped[str | None]
  status: Mapped[str] = mapped_column(default='판매중')
  seller_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
  created_at: Mapped[datetime] = mapped_column(default=datetime.now)

  images: Mapped[list['ProductImage']] = relationship()


class ProductImage(Base):
  __tablename__ = 'product_images'

  id: Mapped[int] = mapped_column(primary_key=True)
  product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
  image_url: Mapped[str]


class Favorite(Base):
  __tablename__ = 'favorites'

  id: Mapped[int] = mapped_column(primary_key=True)
  user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
  product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))

from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from database import engine
from deps import password_hash
from models import User, Product, ProductImage, Favorite


def get_or_create_user(db: Session, username: str):
  user = db.scalar(select(User).where(User.username == username))
  if user is None:
    user = User(username=username, password_hash=password_hash.hash('1234'))
    db.add(user)
    db.flush()
  return user


with Session(engine) as db:
  # 상품 · 사진 · 찜은 지우고 다시 넣는다 (사용자는 그대로 둔다)
  db.execute(delete(Favorite))
  db.execute(delete(ProductImage))
  db.execute(delete(Product))

  seller1 = get_or_create_user(db, 'seller1')
  seller2 = get_or_create_user(db, 'seller2')

  samples = [
    (seller1, '자전거', 50000, '2년 탄 접이식 자전거예요', None, '강남역', '판매중'),
    (seller1, '전공 책', 12000, '필기 조금 있어요', 3000, None, '예약중'),
    (seller2, '무선 이어폰', 30000, '한 번도 안 썼어요', 3000, '홍대입구역', '거래완료'),
  ]

  for i, (seller, title, price, description, shipping_fee, meeting_place, status) in enumerate(samples, start=1):
    product = Product(
      title=title,
      price=price,
      description=description,
      shipping_fee=shipping_fee,
      meeting_place=meeting_place,
      status=status,
      seller_id=seller.id,
    )
    db.add(product)
    db.flush()
    db.add(ProductImage(product_id=product.id, image_url=f'/images/sample{i}.jpg'))

  db.commit()
  print('시드 완료: 사용자 2명 · 상품 3개')

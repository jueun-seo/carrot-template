## 데이터 모델링
목표: 상품 목록 화면에 상품 이미지 · 제목 · 가격 · 위치 · 업로드 시간이 보인다 (검색 창 · 필터는 나중에)
지금: 여기까지(서버) 올릴지 정할 차례

1. 약속 — 상품 정보: 제목 · 가격 · 상품등록일 · 상품상태 · 상품설명 · 배송비 · 직거래희망장소
2. 약속 — 상품에 사진 · 판매자 정보 칸이 더 필요
3. 위치 — 찜은 새 표에 저장
4. 약속 — 찜 표에는 누가 · 어떤 상품을 찜했는지 저장
5. 약속 — 사진은 여러 장, 별도 표에 저장
6. 약속 — 사진 표에는 어떤 상품의 사진인지 · 사진 파일 주소를 저장
7. 약속 — 상품의 판매자는 users 표와 이어 둠
8. 순서 — 학생이 상품 상세의 판매자 정보에 판매자 사진 · 평점 · 후기 · 거래내역 · 팔로우를 넣고 싶다고 함 (추가 기능 후보)
9. 순서 — 판매자 추가 기능은 필수 다섯 뒤 확장 단계에서 정함
10. 이름 — products · product_images · favorites 표와 칸 이름 확정, status는 판매중 · 예약중 · 거래완료 (SPEC 데이터 모델 표에 적음)
11. 약속 — shipping_fee는 비워 둘 수 있음
12. 약속 — meeting_place는 비워 둘 수 있음 (학생: 온라인 거래면 비워두려고)
13. 코드 — backend/models.py에 Product · ProductImage · Favorite 추가 (나머지 칸은 필수)
14. 약속 — 시드 상품은 3개
15. 약속 — 시드 판매자는 seller1 · seller2 두 명
16. 코드 — backend/seed.py 새 파일 (seller1 · seller2, 상품 3개, 사진은 임시 주소)
17. 코드 — 리비전 43781a00dda1 생성 · alembic upgrade head 적용 · seed.py 실행
18. 확인 — (Claude가 DB에서 확인) products 3줄: 자전거(판매중) · 전공 책(예약중) · 무선 이어폰(거래완료), 배송비 · 직거래 장소 비운 줄 있음
19. 코드 — 커밋 77785b5 "상품 · 사진 · 찜 표와 시드 추가"를 main에 올림 (Claude가 git으로 확인: origin/main에 같은 커밋 있음)

## 상품 목록
목표: 상품 목록 화면에 상품 이미지 · 제목 · 가격 · 위치 · 업로드 시간이 보인다 (검색 창 · 필터는 나중에)
지금: 여기까지(서버) 올릴지 정할 차례

1. 순서 — 혼자서 필수 다섯을 순서대로 (상품 목록부터)
2. 약속 — 목록에 보일 것: 검색 창 · 검색 필터 · 이미지들 · 제목 · 가격 · 위치 · 업로드 시간
3. 순서 — 검색 창 · 검색 필터는 목록을 먼저 만든 뒤 나중에 붙임
4. 위치 — Home.jsx 화면에 상품 목록 표시
5. 나누기 — 상품 하나를 components/ 폴더의 컴포넌트로 뺌
6. 이름 — ProductCard와 ProductItem 둘 다 만들기로 함
7. 나누기 — ProductCard는 Home 목록에서 상품 하나하나, ProductItem은 클릭해서 들어간 상세 화면의 상품 (ProductItem은 상품 상세 때 만듦)
8. 순서 — 뼈대(글자만)부터 ProductCard.jsx 만들고 Home.jsx에서 불러 씀
9. 에러 — 5173 주소에 insta 화면이 뜸 · alice 로그인 안 됨: insta 화면 서버(vite)가 5173을 차지하고 있었음
10. 에러 — 로그인 Failed to fetch: carrot 화면이 5174에서 켜졌는데 서버(main.py)는 5173 주소만 허용함 (insta 서버가 아직 5173을 차지)
11. 에러 — 로그인 후 빈 화면: Home.jsx에 ProductCard import 없음 + ProductCard.jsx의 return 다음 줄바꿈 (import 추가, return 뒤에 괄호로 감쌈)
12. 확인 — 로그인 후 Home 화면에 "자전거 · 5000원, 강남역"이 보임 (ProductCard 안에 적어 둔 가짜 값)
13. 약속 — Home이 ProductCard에게 상품 하나를 통째로 product 하나로 넘김
14. 코드 — ProductCard는 product를 받아 title · price · meeting_place를 보여 줌, Home은 가짜 상품 하나를 만들어 넘김 (칸 이름은 DB 칸 이름 그대로)
15. 순서 — 가짜 상품 여러 개를 배열에 담고 map으로 반복해서 그리기
16. 코드 — Home.jsx의 product1 · 2 · 3을 products 배열 하나로 묶고 map으로 ProductCard 반복 (상품마다 id를 넣고 key로 씀)
17. 출처 — /docs에서 상품 주소 찾기 → 학생이 없음을 확인 (auth 묶음만 있음)
  18. 순서 — 서버에 상품 목록 주소를 만들러 내려감
  19. 확인 — 학생이 DB 도구로 products에 상품 3줄이 있는 걸 직접 확인
  20. 약속 — GET /api/products
  21. 약속 — 응답은 products 표에 들어 있는 데이터 (확인 중)
  22. 확인 — 목록의 위치는 products의 meeting_place, 이미지는 products에 없고 product_images에 있음을 학생이 확인
  23. 약속 — 응답의 상품 하나에 products의 데이터와 images(사진 주소 목록)를 함께 넣음
  24. 나누기 — 상품 관련 주소는 새 파일 routers/products.py에 모음
  25. 약속 — 로그인 없이도 상품 목록을 볼 수 있음
  26. 코드 — routers/products.py 새 파일(GET /api/products) · schemas.py에 ProductOut · models.py Product에 images 관계 · main.py에 라우터 연결 (Claude가 curl로 확인: 상품 3개와 images가 옴)
  27. 약속 — 바꿈: images를 사진 주소 글자 목록이 아니라 객체 목록(id · image_url)으로 줌 (학생: 그러면 products.py 코드를 줄일 수 있어서)
  28. 코드 — schemas.py에 ImageOut 추가, ProductOut.images를 ImageOut 목록으로, products.py는 DB에서 꺼낸 상품을 그대로 return (Claude가 curl로 확인)
  29. 확인 — 학생이 /docs에서 GET /api/products가 상품 3개를 ProductOut 모양(images 포함)으로 돌려주는 것을 확인

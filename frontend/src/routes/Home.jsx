import ProductCard from '../components/ProductCard.jsx'

function Home() {
  const products = [
    { id: 1, title: '자전거', price: 1000, meeting_place: '강남역' },
    { id: 2, title: '이불', price: 1000, meeting_place: '강남역' },
    { id: 3, title: '장난감', price: 1000, meeting_place: '강남역' },
  ]

  return (
    <>
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </>
  )
}

export default Home

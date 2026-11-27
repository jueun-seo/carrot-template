function ProductCard({ product }) {
    return (
    <div>
        <h5>{product.title}</h5>
        <p>{product.price}원, {product.meeting_place}</p>
    </div>
    )
}

export default ProductCard

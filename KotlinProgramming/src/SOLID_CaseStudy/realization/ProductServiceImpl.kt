package SOLID_CaseStudy.realization

class ProductServiceImpl: ProductService {
    override fun getProduct(id: String) {
        println("Call override get Product $id")
    }

    override fun calculateProductPrice() {
        println("Price: Rp 50.000")
    }
}
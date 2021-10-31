package SOLID_CaseStudy.realization

fun main() {
    val productServiceImpl = ProductServiceImpl()
    productServiceImpl.getProduct("12345")
    productServiceImpl.calculateProductPrice()
}
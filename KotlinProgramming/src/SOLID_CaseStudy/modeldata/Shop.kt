package SOLID_CaseStudy.modeldata

class Shop(
    private val id: Int,
    val name: String
) {
    var seller: Seller
        set(value) {
            seller = value
        }
        get() {
            return seller
        }
}
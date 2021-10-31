package SOLID_CaseStudy.kardinalitas.onetomany

class Seller(
    private val id: Int,
    val name: String
)

class User(
    private val id: Int,
    val name: String,
    val sellers: List<Seller>
)
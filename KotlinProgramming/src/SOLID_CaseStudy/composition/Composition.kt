package SOLID_CaseStudy.composition

import SOLID_CaseStudy.modeldata.Address
import SOLID_CaseStudy.modeldata.User

fun main() {
    val user = User(
        id = 1234,
        name = "Algokelvin",
        address = Address(123, "Bandung")
    )
    println("Name: " + user.name)
    println("Address: " + user.address?.location)
}
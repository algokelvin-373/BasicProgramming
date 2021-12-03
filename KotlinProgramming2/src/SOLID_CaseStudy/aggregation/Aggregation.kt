package SOLID_CaseStudy.aggregation

import SOLID_CaseStudy.modeldata.Seller
import SOLID_CaseStudy.modeldata.Shop

fun main() {
    val shop = Shop(20, "Olshop.vin")
    shop.seller = Seller(1234, "Cindy - KK Indonesia")
    println("All Seller " + shop.name)
    println(shop.seller.name)
}
package SOLID_CaseStudy.kardinalitas.onetomany

import SOLID_CaseStudy.modeldata.Seller
import SOLID_CaseStudy.modeldata.User

/*
    Implement One to Many
    ' User and Seller '
*/

fun main() {
    // Data Seller
    val dataSeller = ArrayList<Seller>()
    dataSeller.add(Seller(1234, "Cindy - KK Indonesia"))
    dataSeller.add(Seller(5463, "Kelvin - Olshop.vin"))
    dataSeller.add(Seller(9876, "Belle - CandyCake"))
    dataSeller.add(Seller(4563, "Putri - CoffeeTop"))
    dataSeller.add(Seller(7421, "Hendri - Official Huawei"))

    // Data User
    val dataUser = ArrayList<User>()
    dataUser.add(User(1, "Indri", listOf(dataSeller[0], dataSeller[2])))
    dataUser.add(User(2, "Yanti", listOf(dataSeller[1])))
    dataUser.add(User(3, "Iqbal", listOf(dataSeller[3], dataSeller[4], dataSeller[1])))

    for (x in 0 until dataUser.size) {
        println("- ${dataUser[x].name} -")
        dataUser[x].sellers.forEach {
            println(it.name)
        }
        println()
    }

}
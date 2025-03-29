package casestudy._03

import java.text.DecimalFormat
import java.text.NumberFormat

fun convertCurrency(data: Double): String {
    val formatter: NumberFormat = DecimalFormat("#,###")
    return formatter.format(data).replace(",", ".")
}

fun main() {
    println(convertCurrency(5000.0))
    println(convertCurrency(50000.0))
    println(convertCurrency(500000.0))
    println(convertCurrency(5000000.0))
}
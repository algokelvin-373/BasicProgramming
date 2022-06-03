package m018_elvis_operator

fun main() {
    val b: String? = null // nullable type

    // Implement elvis operator
    val a = b?.length ?: 0

    println(a)
}
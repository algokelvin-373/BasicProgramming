package m016_nullable_type

fun main() {
    // val a: String = null  ==> error
    val b: String? = null // solved - nullable type

    // println(b.length) ==> error
    if (b != null) { // solved - using if expression
        println(b.length)
    }
}
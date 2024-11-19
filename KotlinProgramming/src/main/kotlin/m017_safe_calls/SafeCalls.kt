package m017_safe_calls

fun main() {
    val b: String? = null // nullable type
    val a = b?.length // safe calls to avoid error
    println(a)
}
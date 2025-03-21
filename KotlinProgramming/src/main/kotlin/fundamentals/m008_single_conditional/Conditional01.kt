package fundamentals.m008_single_conditional

fun main() {
    print("Input number: ")
    val a = readLine() // Input from Keyboard

    // Single Conditional (If)
    if (a?.toInt()!! % 2 == 0) {
        println("$a is even")
    }
    println("Done")
}

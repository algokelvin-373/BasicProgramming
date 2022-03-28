package m010_multi_conditional

fun main() {
    print("Input number: ")
    val a = readLine() // Input from Keyboard

    // Double Conditional (If-Else)
    val num = a
    if (a?.toInt()!! % 2 == 0) {
        println("$a is divided by 2")
    } else if (a.toInt() % 3 == 0) {
        println("$a is divided by 3")
    } else {
        println("$a isn't divided by 2 or 3")
    }
}
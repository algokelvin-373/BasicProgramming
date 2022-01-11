package m004_conditionals

fun main() {
    print("Input number: ")
    val a = readLine() // Input from Keyboard

    // Double Conditional (If-Else)
    if (a?.toInt()!! % 2 == 0) {
        println("$a is even")
    } else {
        println("$a is odd")
    }
}

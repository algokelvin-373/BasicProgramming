package m004_conditionals

fun main() {
    print("Input number: ")
    val a = readLine() // Input from Keyboard
    if (a?.toInt()!! % 2 == 0) {
        println("$a is even")
    } else {
        println("$a is odd")
    }
}
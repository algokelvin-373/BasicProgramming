package fundamentals.m011_when_expression

fun main() {
    print("Input number: ")
    val a = readLine() // Input from Keyboard

    // When Expression
    when {
        a?.toInt()!! % 2 == 0 -> println("$a is divided by 2")
        a.toInt() % 3 == 0 -> println("$a is divided by 3")
        else -> println("$a isn't divided by 2 or 3")
    }
}
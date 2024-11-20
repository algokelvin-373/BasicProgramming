package train

fun main() {
    // When Expressions
    val number = 2

    // Type 1
    when(number) {
        2 -> println("Your number is $number")
        else -> println("You input other number")
    }
    // Type 2
    when {
        number % 2 == 0 -> println("$number is even")
        else -> println("$number is odd")
    }

    // While and Do While
    var count = 1
    var max = 5
    while (count <= max) {
        println("Count: $count")
        count++
    }

    max = 10
    do {
        println("Count: $count")
        count++
    } while (count <= max)
}
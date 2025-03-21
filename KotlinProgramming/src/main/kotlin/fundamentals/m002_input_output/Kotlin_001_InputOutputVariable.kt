package fundamentals.m002_input_output

fun main() { // This is main program Kotlin Language
    // variable 'val' - constant value
    val PI = 3.14
    // PI = 6.28 you cannot chane this value
    println(PI)

    // variable 'var' - you can change value
    var num1 = 100
    println(num1)
    num1 = 200
    println(num1)

    // Input Data
    print("Input word: ")
    val word = readln()

    // Output Data
    println("Your input: $word")
}
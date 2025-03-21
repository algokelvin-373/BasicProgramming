package fundamentals.m012_looping_for

fun main() {
    // Show data 1 until n
    print("Input n: ")
    val n = readLine() // Input from Keyboard

    // Looping 'for'
    for (x in 1..n?.toInt()!!) {
        print("$x ")
    }
    println()

}
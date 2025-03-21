package fundamentals.m013_looping_while

fun main() {
    // Show data 1 until n
    print("Input n: ")
    val n = readLine() // Input from Keyboard

    // Looping 'while'
    var x = 1
    while (x <= n?.toInt()!!) {
        print("$x ")
        x++
    }
    println()

}
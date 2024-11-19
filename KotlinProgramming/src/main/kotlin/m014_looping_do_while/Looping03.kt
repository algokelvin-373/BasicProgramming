package m014_looping_do_while

fun main() {
    // Show data 1 until n
    print("Input n: ")
    val n = readLine() // Input from Keyboard

    // Looping 'do while'
    var x = 1
    do {
        print("$x ")
        x++
    } while (x <= n?.toInt()!!)
    println()

}
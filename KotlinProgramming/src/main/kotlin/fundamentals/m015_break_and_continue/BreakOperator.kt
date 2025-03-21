package fundamentals.m015_break_and_continue

fun main() {
    for (x in 1..15) {
        if (x == 10)
            break
        print("$x ")
    }
    println()
}
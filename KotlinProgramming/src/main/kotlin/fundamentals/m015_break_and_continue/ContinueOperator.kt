package fundamentals.m015_break_and_continue

fun main() {
    for (x in 1..15) {
        if (x % 2 == 0 && x % 3 == 0)
            continue
        print("$x ")
    }
    println()
}
package casestudy._02

import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

fun getTimeNow(format: String): String {
    val current = LocalDateTime.now()
    val formatter = DateTimeFormatter.ofPattern(format)
    return current.format(formatter)
}

fun main() {
    val time = getTimeNow("d MMM yyyy")
    println(time)
}
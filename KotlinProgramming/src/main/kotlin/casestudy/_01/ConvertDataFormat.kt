package casestudy._01

import java.text.SimpleDateFormat
import java.util.*

fun getDateConvert(oldFormat: String, oldDate: String, newFormat: String): String {
    val sdf = SimpleDateFormat(oldFormat, Locale.getDefault())
    val sdf2 = SimpleDateFormat(newFormat, Locale("id","ID"))
    val date = sdf.parse(oldDate)
    return sdf2.format(date)
}

fun main() {
    val dateFormat = getDateConvert(
        "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
        "2001-07-04T12:08:56.235-0700",
        "d MMM yyyy"
    )
    println(dateFormat)
}
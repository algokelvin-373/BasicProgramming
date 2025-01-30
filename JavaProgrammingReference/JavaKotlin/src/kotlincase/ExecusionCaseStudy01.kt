package kotlincase

fun main() {
    //Case 1: Convert Format Date
    val dateFormat = CaseStudy01.getDateConvert(
        "yyyy-MM-dd'T'HH:mm:ss.SSSZ",
        "2001-07-04T12:08:56.235-0700",
        "d MMM yyyy"
    )
    println(dateFormat)
}

package com.dicoding.exam.optionalexam3

// TODO
fun manipulateString(str: String, int: Int): String {
    var finalResult = ""
    val regex = "([A-Za-z]+)(\\d+)"

    val containsDigit = str.any { it.isDigit() }
    if (containsDigit) {
        val matchResult = Regex(regex).find(str)
        if (matchResult != null) {
            val (textStr, numberStr) = matchResult.destructured
            val numberResult = numberStr.toInt() * int
            finalResult = textStr + numberResult.toString()
        }
    } else {
        finalResult = str + int
    }

    return finalResult
}

package com.dicoding.exam.optionalexam4

// TODO
fun getMiddleCharacters(string: String): String {
    val charStr = string.toCharArray()
    val size = string.length
    val median = size / 2
    return if (size % 2 == 0) {
        charStr[median - 1].toString() + charStr[median].toString()
    } else {
        charStr[median].toString()
    }
}
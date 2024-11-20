package com.dicoding.exam.optionalexam2

// TODO
fun minAndMax(number: Int): Int {
    val listDigits = number.toString().map { data ->
        data.toString().toInt()
    }.toSet()
    val max = listDigits.max()
    val min = listDigits.min()

    return min + max
}

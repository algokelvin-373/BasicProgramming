package com.dicoding.exam.optionalexam1

// TODO
fun sumOfBigThree(vararg numbers: Int): Int {
    numbers.sortDescending()
    val data = numbers.take(3)
    return data.sum()
}

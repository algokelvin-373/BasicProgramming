package com.youtube.kotlin_code._03_IfElseStatement

fun main() {
    // If Else Statement

    print("Input a: ")
    val numA = readln().toInt()

    print("Input b: ")
    val numB = readln().toInt()

    if (numA > numB) {
        println("A is bigger than B")
    } else if (numA == numB) {
        println("A is same with B")
    } else {
        println("B is bigger than A")
    }

}
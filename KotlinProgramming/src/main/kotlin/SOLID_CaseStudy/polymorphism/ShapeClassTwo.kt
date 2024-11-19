package SOLID_CaseStudy.polymorphism

abstract class ShapeClassTwo {
    fun area(radius: Double): Double { // Area of Circle
        return Math.PI * radius *  radius
    }
    fun area(width: Int, height: Int): Int { // Area of Rectangle
        return width * height
    }
}

class CircleTwo(private val radius: Double): ShapeClassTwo() {
    fun calculateArea(): Double { // Polymorphism for area circle
        return super.area(radius)
    }
}

class RectangleTwo(private val width: Int, private val height: Int): ShapeClassTwo() {
    fun calculateArea(): Int { // Polymorphism for area rectangle
        return super.area(width, height)
    }
}

fun main() {
    val circleTwo = CircleTwo(7.0)
    val rectangleTwo = RectangleTwo(10, 20)
    println("Area Circle    : ${circleTwo.calculateArea()}")
    println("Area Rectangle : ${rectangleTwo.calculateArea()}")
}

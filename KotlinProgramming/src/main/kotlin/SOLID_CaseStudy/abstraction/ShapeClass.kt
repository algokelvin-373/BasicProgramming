package SOLID_CaseStudy.abstraction

abstract class Shape {
    abstract fun area(): Double
}

class Circle(private val radius: Double): Shape() {
    override fun area(): Double {
        return Math.PI * radius * radius
    }
}

class Rectangle(private val width: Double, private val height: Double): Shape() {
    override fun area(): Double {
        return width * height
    }
}

fun main() {
    val circle = Circle(7.0)
    val rectangle = Rectangle(10.0, 20.0)
    println("Area Circle    : ${circle.area()}")
    println("Area Rectangle : ${rectangle.area()}")
}

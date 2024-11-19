package SOLID_CaseStudy.inheritance

open class Animal {
    fun walk() {
        println("${javaClass.simpleName} walk! on class Animal")
    }
}

class Cow: Animal() {
    fun play() {
        println("${javaClass.simpleName} play! on class Cat")
    }
}

fun main() {
    val cow = Cow()
    cow.walk()
    cow.play()
}
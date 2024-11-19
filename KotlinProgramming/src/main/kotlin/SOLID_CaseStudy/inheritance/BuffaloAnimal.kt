package SOLID_CaseStudy.inheritance

open class Herbivore: Animal() {
    fun herbivore() {
        println("${javaClass.simpleName} is Herbivore! on class Herbivore")
    }
}

class Buffalo: Herbivore() {
    fun play() {
        println("${javaClass.simpleName} play! on class Buffalo")
    }
}

fun main() {
    val buffalo = Buffalo()
    buffalo.walk()
    buffalo.herbivore()
    buffalo.play()
}
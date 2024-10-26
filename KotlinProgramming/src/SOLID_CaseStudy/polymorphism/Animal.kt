class Animal {
    fun walk() {
        println("${javaClass.simpleName} walk! on class Animal")
    }
}

class Cat: Animal {
    override fun walk() {
        super.walk()
        println("${javaClass.simpleName} walk! on class Cat")
    }
}

fun main() {
    val cat = Cat()
    cat.walk()
}
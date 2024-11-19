package SOLID_CaseStudy.encapsulation

class Person {
    // Make private - Encapsulations
    private var name = ""

    fun setName(name: String) {
        this.name = name
    }

    fun getName(): String {
        return name
    }
}

fun main() {
    val person = Person()
    person.setName("Kelvin")
    println(person.getName())
}

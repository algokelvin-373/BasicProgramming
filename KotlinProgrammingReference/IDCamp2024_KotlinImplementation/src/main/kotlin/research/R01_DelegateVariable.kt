package research

import kotlin.reflect.KProperty

class DelegateVar {
    private var value: String = "Default"

    operator fun getValue(classRef: Any?, property: KProperty<*>) : String {
        println("Fungsi ini sama seperti getter untuk properti ${property.name} pada class $classRef")
        return value
    }

    operator fun setValue(classRef: Any?, property: KProperty<*>, newValue: String){
        println("Fungsi ini sama seperti setter untuk properti ${property.name} pada class $classRef")
        println("Nilai ${property.name} dari: $value akan berubah menjadi $newValue")
        value = newValue
    }
}

class Person {
    var name: String by DelegateVar()
    var birthday: String by DelegateVar()
}

fun main() {
    val person = Person()
    person.name = "Kelvin"
    person.birthday = "17 May 96"

    println("Name\t\t: ${person.name}")
    println("Birthday\t: ${person.birthday}")
}
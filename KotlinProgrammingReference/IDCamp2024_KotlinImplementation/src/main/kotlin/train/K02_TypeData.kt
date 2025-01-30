package train

fun main() {
    // Default Value
    var dataStr = "Kotlin" // data type String
    var dataNumber = 100 // data type Number (Integer)
    var dataChar = 'K' // data type Char

    println("---[Default Value]---")
    print("Value dataStr\t\t: $dataStr \n")
    print("Value dataNumber\t: $dataNumber \n")
    print("Value dataChar\t\t: $dataChar \n")

    // Change Value
    dataStr = "Kotlin Implementation" // change value data type String
    dataNumber = 200 // change value data type Int
    dataChar++ // change value data char

    println("---[Change Value]---")
    print("Value dataStr\t\t: $dataStr \n")
    print("Value dataNumber\t: $dataNumber \n")
    print("Value dataChar\t\t: $dataChar \n")
}
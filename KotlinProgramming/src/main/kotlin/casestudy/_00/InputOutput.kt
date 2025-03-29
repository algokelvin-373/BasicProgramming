package casestudy._00

fun main() {
    print("Input Data: ")
    val data = readlnOrNull()
    if (data == "") {
        println("Your Data: Empty Data")
    } else {
        println("Your Data: $data")
    }
}
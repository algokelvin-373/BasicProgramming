package casestudy._05

fun main() {
    print("Input Your Word: ")
    val inputWord = readlnOrNull()
    val capitalizedString = inputWord?.split(" ")
        ?.joinToString(" ") {
            it.replaceFirstChar {
                    char -> char.uppercase()
            }
        }
    println("String with first capital: $capitalizedString")
}
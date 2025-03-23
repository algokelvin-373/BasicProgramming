package casestudy._05

fun makingFirstCapital(inputWord: String) {
    val capitalizedString = inputWord.split(" ")
        .joinToString(" ") {
            it.replaceFirstChar {
                char -> char.uppercase()
            }
        }
    println("String with first capital: $capitalizedString")
}

fun main() {
    print("Input Your Word: ")
    val inputWord = readlnOrNull() ?: ""
    makingFirstCapital(inputWord)
}
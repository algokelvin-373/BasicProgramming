package casestudy._04

fun strManipulation(inputWord: String) {
    val reversedStr = inputWord.reversed()
    println("Reverse String: $reversedStr")

    val countChar = inputWord.length
    println("Count Char: $countChar")

    val trimmedString = inputWord.trim()
    val noExtraSpaces = trimmedString.replace("\\s+".toRegex(), " ")
    println("String tanpa spasi berlebih: $noExtraSpaces")
}

fun main() {
    print("Input Your Word: ")
    val inputWord = readlnOrNull() ?: ""
    if (inputWord == "") {
        println("Empty Input Data")
    } else {
        strManipulation(inputWord)
    }
}
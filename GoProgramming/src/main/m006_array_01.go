package main

import "fmt"

func main() {
	var numbers = [5] int {1, 2, 3, 4, 5} // Array Integer
	var text = [3] string {"Algokelvin", "Algorithm", "Master"} // Array String

	fmt.Println("Count numbers: ", len(numbers))
	fmt.Println("Data numbers : ", numbers)

	fmt.Println("")

	fmt.Println("Count text: ", len(text))
	fmt.Println("Data text : ", text)
}
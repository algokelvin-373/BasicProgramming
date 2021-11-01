package main

import "fmt"

func main() {
	// Array Without Count Elemen

	// Number 1
	var numbers = [...] int {1, 2, 3}
	for x := 0; x < len(numbers); x++ {
		fmt.Println("Data numbers : ", numbers[x])
	}

}
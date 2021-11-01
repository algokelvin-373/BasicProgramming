package main

import "fmt"

func main() {
	// Looping Array 2
	var numbers[5] int

	for x := 0; x < len(numbers); x++ {
		numbers[x] = x * 2
		fmt.Println("Data numbers : ", numbers[x])
	}
}
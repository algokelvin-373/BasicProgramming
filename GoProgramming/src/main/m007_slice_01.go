package main

import "fmt"

func main() {
	// Inizialization Slice
	var numbers = [] int {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

	var numbers1 = numbers[0:4] // Show index 0 until 4
	var numbers2 = numbers[:2] // Show index 0 until 2
	var numbers3 = numbers[7:] // Show index 7 until end
	var numbers4 = numbers[5:len(numbers)] // Show index 5 until end
	var numbers5 = numbers[:] // Show all element
	var numbers6 = numbers[2:2] // Show empty slice

	fmt.Println("Numbers1 : ", numbers1)
	fmt.Println("Numbers2 : ", numbers2)
	fmt.Println("Numbers3 : ", numbers3)
	fmt.Println("Numbers4 : ", numbers4)
	fmt.Println("Numbers5 : ", numbers5)
	fmt.Println("Numbers6 : ", numbers6)
	
}
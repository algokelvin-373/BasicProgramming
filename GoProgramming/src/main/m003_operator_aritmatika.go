package main

import "fmt"

func main() {
	var a, b = 10, 3
	var rPlus = a + b
	var rMinus = a - b
	var rTimes = a * b
	var rDivided = a / b
	var rModule = a % b

	fmt.Println("a + b = ", rPlus)
	fmt.Println("a - b = ", rMinus)
	fmt.Println("a * b = ", rTimes)
	fmt.Println("a / b = ", rDivided)
	fmt.Println("a % b = ", rModule)
}


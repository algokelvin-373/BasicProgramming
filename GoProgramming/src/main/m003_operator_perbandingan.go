package main

import "fmt"

func main() {
	var a, b, c, d = 5, 10, 20, 40

	// Operator '=='
	var a1, a2 = b / a, c / b
	fmt.Println("a1 == a2 >> ", a1 == a2)

	// Operator '!='
	fmt.Println("c != d >> ", c != d)

	// Operator '>', '>=', '<', and '<='
	var b1, b2 = c / a, d / c
	var b3 = b2
	fmt.Println("b1 > b2 >> ", b1 > b2)
	fmt.Println("b3 >= b2 >> ", b3 >= b2)
	fmt.Println("b2 < b1 >> ", b2 < b1)
	fmt.Println("b2 <= b3 >> ", b2 <= b3)
}
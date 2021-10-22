package main

import "fmt"

func main() {
	// Using type variable
	var a, b, c int
	a = 3; b = 4; c = 5;
	fmt.Println("Initialize Variable Integer And Set Number")
	fmt.Println("a = ", + a)
	fmt.Println("b = ", + b)
	fmt.Println("c = ", + c)

	// Without set type variable
	d := 10; e := 20; f := 30;
	fmt.Println("Initialize Variable Set Number in Integer")
	fmt.Println("d = ", + d)
	fmt.Println("e = ", + e)
	fmt.Println("f = ", + f)

	// Set Data Witt 'var' but not set type variable
	var g, h, i = 100, 200, 300
	fmt.Println("Initialize Variable With 'var' But Not Set Variable")
	fmt.Println("g = ", + g)
	fmt.Println("h = ", + h)
	fmt.Println("i = ", + i)
}
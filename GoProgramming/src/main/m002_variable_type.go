package main

import "fmt"

func main() {
	// Using Initialize Variable
	var a int // initialize 'int'
	var b float32 // initialize 'float32'
	var c string // initialize 'string'
	var x bool // initilialize 'boolean'
	a = 1; b = 3.14; c = "Algokelvin"; x = true;
	fmt.Println("a = ", + a) 
	fmt.Println("b = ", + b)
	fmt.Println("c = ", c)
	fmt.Println("x = ", x)

	// Without Initialize Variable
	var d, e, f, y = 10, 1.41, "Algokelvin 2", true
	fmt.Println("d = ", + d) 
	fmt.Println("e = ", + e)
	fmt.Println("f = ", f)
	fmt.Println("y = ", y)

}
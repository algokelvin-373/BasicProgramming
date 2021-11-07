package main

import "fmt"

func main() {
	// Multi Predefined return
	var s = 10.0
	var area, circumference = calculateRectangle(s)
	fmt.Println("Calculate Rectangle ( s = ",s," )")
	fmt.Println("Circumference: ", circumference)
	fmt.Println("Area         : ", area)
}

func calculateRectangle(s float64) (area float64, circumference float64) {
	circumference = 4 * s
	area = s * s
	return
}

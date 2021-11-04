package main

import "fmt"

func main() {
	// Multi return
	var s = 10.0
	var area, circumference = calculateRectangle(s)
	fmt.Println("Calculate Rectangle ( s = ",s," )")
	fmt.Println("Circumference: ", circumference)
	fmt.Println("Area         : ", area)
}

func calculateRectangle(s float64) (float64, float64) {
	var circumference = 4 * s
	var area = s * s
	return area, circumference
}

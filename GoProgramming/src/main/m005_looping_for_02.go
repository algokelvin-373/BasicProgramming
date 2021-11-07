package main

import "fmt"

// Just using argument condition
func main() {
	var x = 0
	for x < 5 {
		fmt.Println("Algokelvin ", x + 1 , " time")
		x++
	}
}
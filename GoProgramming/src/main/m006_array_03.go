package main

import "fmt"

func main() {
	// Looping Array 1
	var text = [3] string {
		"Algokelvin", 
		"Algorithm", 
		"Master"}

	for x := 0; x < len(text); x++ {
		fmt.Println("Data text : ", text[x])
	}
}
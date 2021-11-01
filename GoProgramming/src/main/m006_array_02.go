package main

import "fmt"

func main() {
	// Inizialization Array Type 1
	var names1 [4] string
	names1[0] = "Algokelvin"
	names1[1] = "Jenna"
	names1[2] = "Deddy"
	names1[3] = "Miawaug"

	fmt.Println("Count names1: ", len(names1))
	fmt.Println("Data names1 : ", names1)

	fmt.Println("")

	// Inizialization Array Type 2
	var names2 = [4] string {
		"Algokelvin",
		"Jenna",
		"Deddy",
		"Miawaug" }

	fmt.Println("Count names2: ", len(names2))
	fmt.Println("Data names2 : ", names2)

	fmt.Println("")

}
package main

import "fmt"

// Create struct 'profile'
type people struct {
	name string
	gender string
}

type profile struct {
	id int
	people
}

// Inizialize Embedeed Struct 1
func main() {
	var s = profile {1, people{"Algokelvin", "male"}}

	fmt.Println(s.id)
	fmt.Println(s.name)
	fmt.Println(s.gender)
}

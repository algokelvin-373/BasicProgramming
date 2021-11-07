package main

import "fmt"

// Create struct 'profile'
type profile struct {
	id int
	name string
}

// Inizialize 'struct' type 1
func main() {
	var s profile
	s.id = 1
	s.name = "Algokelvin"

	fmt.Println(s.id)
	fmt.Println(s.name)
}

package main

import "fmt"

// Create struct 'profile'
type profile struct {
	id int
	name string
}

// Inizialize 'struct' type 3
func main() {
	var s = profile {1, "Algokelvin"}

	fmt.Println(s.id)
	fmt.Println(s.name)
}

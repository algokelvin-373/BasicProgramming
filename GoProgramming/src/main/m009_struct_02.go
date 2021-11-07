package main

import "fmt"

// Create struct 'profile'
type profile struct {
	id int
	name string
}

// Inizialize 'struct' type 2
func main() {
	var s = profile {id: 1, name: "Algokelvin"}

	fmt.Println(s.id)
	fmt.Println(s.name)
}

package main
import "fmt"

type people struct {
	name string
	gender string
}

type profile struct {
	id int
	people
}

// Inizialize Embedeed Struct 2
func main() {
	var s = profile {}
	s.id = 1
	s.name = "Algokelvin"
	s.gender = "male"

	fmt.Println(s.id)
	fmt.Println(s.name)
	fmt.Println(s.gender)
}

package main
import "fmt"

type people struct {
	id int
	name string
	gender string
}

func (p people) sayHello() {
	fmt.Println("Hi, ", p.name)
}

// Inizialize 'Method'
func main() {
	var p1 = people{1, "Algokelvin", "Male"}
	p1.sayHello()
}

package main

import "fmt"

func main() {
	var a = 7

	switch a {
		// Multicase
		case 2, 3, 5, 7: 
			fmt.Println(a ,": bilangan prima")
		default: 
			fmt.Println(a ,": bukan bilangan prima")
	}
}


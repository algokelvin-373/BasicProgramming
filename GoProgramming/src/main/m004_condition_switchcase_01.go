package main

import "fmt"

func main() {
	var a = 8

	switch a {
		case 8: 
			fmt.Println("Your set a -> 8")
			fmt.Println("Show in case 8")
		case 9: 
			fmt.Println("Your set a -> 9")
			fmt.Println("Show in case 9")
		default: fmt.Println("Your set a other number")
	}
}
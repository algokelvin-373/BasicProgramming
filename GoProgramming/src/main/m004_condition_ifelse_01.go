package main

import "fmt"

func main() {
	var a = 4
	if a % 2 == 0 {
		fmt.Println(a ," : bilangan genap")
	} else {
		fmt.Println(a ," : bilangan ganjil")
	}
}
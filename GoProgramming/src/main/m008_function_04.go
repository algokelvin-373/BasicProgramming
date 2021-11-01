package main

import "fmt"

func main() {
	// With params and return
	var data = showMessage("Go")
	fmt.Println(data, "Programming Fundamental")
}

func showMessage(msg string) string {
	return msg
}

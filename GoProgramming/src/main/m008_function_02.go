package main

import "fmt"

func main() {
	// With return, without params
	var data = showMessage()
	fmt.Println(data, "Programming returns")
}

func showMessage() string {
	return "Go"
}

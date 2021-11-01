package main

import "fmt"

func main() {
	// With params, without return
	showMessage("Go Programming Params")
}

func showMessage(msg string) {
	fmt.Println(msg)
}

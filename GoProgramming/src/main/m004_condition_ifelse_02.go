

package main

import "fmt"

func main() {
	var a = 25
	if a > 10 && a <= 20 {
		fmt.Println(a ," lebih dari 10")
	} else if a > 20 {
		fmt.Println(a ," lebih dari 20")
	} else {
		fmt.Println(a ," kurang dari 10")
	}
}




package main

import "fmt"

// Without argument
func main() {
	var x = 0
	for {
		fmt.Println("Algokelvin ", x + 1 , " time")
		x++

		// To Stop Looping Using 'break'
		if (x == 5) {
			break
		}
	}
}



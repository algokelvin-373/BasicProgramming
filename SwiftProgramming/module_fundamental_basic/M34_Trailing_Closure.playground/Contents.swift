import UIKit

let digitNames = [
   0: "Zero", 1: "One", 2: "Two",   3: "Three", 4: "Four",
   5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
]
let numbers = [36, 42, 198]

// Trailing Closure ( see like that lambda in Kotlin )
let numberStrings = numbers.map { (number) -> String in
   var number = number
   var output = ""
   repeat {
       output = digitNames[number % 10]! + output
       number /= 10
   } while number > 0
   return output
}
print(numberStrings)

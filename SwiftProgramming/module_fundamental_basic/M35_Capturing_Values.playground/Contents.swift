import UIKit

// Capturing Values
func makeIncrementer(forIncrement amount: Int) -> () -> Int {
   var runningTotal = 0
   func incrementer() -> Int {
       runningTotal += amount
       return runningTotal
   }
   return incrementer
}

// Increment ten
let incrementByTen = makeIncrementer(forIncrement: 10)

incrementByTen()
incrementByTen()
incrementByTen()
incrementByTen()
print(incrementByTen())

// Increment eight
let incrementByEight = makeIncrementer(forIncrement: 8)
for _ in 0...5 {
    print(incrementByEight())
}

// Closures Are Reference Types
let alsoIncrementByEight = incrementByEight
alsoIncrementByEight()
print(alsoIncrementByEight())

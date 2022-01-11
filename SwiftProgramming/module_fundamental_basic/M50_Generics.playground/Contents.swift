import UIKit

func swapTwoValues<T>(_ a: inout T, _ b: inout T) {
   let temporaryA = a
   a = b
   b = temporaryA
}

var someInt = 100
var anotherInt = 200
print("Before swap: someInt -> \(someInt) && anotherInt -> \(anotherInt)")
swapTwoValues(&someInt, &anotherInt)
print("After swap: someInt -> \(someInt) && anotherInt -> \(anotherInt)")

 
var someString = "Dicoding"
var anotherString = "Indonesia"
print("Before swap: someInt -> \(someString) && anotherInt -> \(anotherString)")
swapTwoValues(&someString, &anotherString)
print("After swap: someInt -> \(someString) && anotherInt -> \(anotherString)")

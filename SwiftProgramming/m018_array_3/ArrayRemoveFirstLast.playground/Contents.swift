
import Cocoa

var arrayInt = [4, 1, 2, 6, 3, 0]
print("Before : \(arrayInt)")

// remove first data
arrayInt.removeFirst()
print("After 1: \(arrayInt)")

// remove last data
arrayInt.removeLast()
print("After 2: \(arrayInt)")


import Cocoa

var arrayInt = [4, 1, 2, 6, 3, 0]
print("Before : \(arrayInt)")

// Replace
arrayInt[2] = 200
print("After 1: \(arrayInt)")

// Replace with Range
arrayInt[3...5] = [60, 30, 10]
print("After 2: \(arrayInt)")

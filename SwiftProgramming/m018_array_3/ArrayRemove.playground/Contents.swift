
import Cocoa

var arrayInt = [4, 1, 2, 6, 3, 0]
print("Before : \(arrayInt)")

// remove data in index 5
arrayInt.remove(at: 5)
print("After 1: \(arrayInt)")

// remove data in index 2
arrayInt.remove(at: 2)
print("After 2: \(arrayInt)")

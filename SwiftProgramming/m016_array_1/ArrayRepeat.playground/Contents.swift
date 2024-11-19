
import Cocoa

var arrayInt = [Int]();

// Repeating input data 15 three times
var repeatingInt = Array(repeating: 15, count: 3)

arrayInt += repeatingInt

print("Data Array: \(arrayInt)")
print("Amount Data Array Int: \(arrayInt.count)")

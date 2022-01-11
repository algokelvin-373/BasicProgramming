import UIKit

/* Array Integer */

// Array Count & Empty
var arrayInt = [Int](); print("Amount Data Array Int: \(arrayInt.count)")
if arrayInt.isEmpty {
    print("This ArrayInt is empty")
}
print("----------")

// Array append ( Input data in last index, same likes PUSH in Stack )
arrayInt.append(2)
arrayInt.append(4)
print("Data Array: \(arrayInt)")
print("Amount Data Array Int: \(arrayInt.count)")
print("----------")

// Repeat creating data Array
var repeatingInt = Array(repeating: 15, count: 3) // Repeating input data 15 three times
arrayInt += repeatingInt
print("Data Array: \(arrayInt)")
print("Amount Data Array Int: \(arrayInt.count)")
print("----------")

// Plus data Array
arrayInt += [4, 1, 2] + [6, 3, 0]
print("Data Array: \(arrayInt)")
print("Amount Data Array Int: \(arrayInt.count)")
print("----------")

// Print data array in some index
print("arrayInt[2] = \(arrayInt[2])")
print("arrayInt[7] = \(arrayInt[7])")
print("----------")

// Replace data array in some index
arrayInt[9] = 100 // Replace data array in index 9
print("Data Array: \(arrayInt)")
arrayInt[3...6] = [300, 250, 100, 50] // Replace data array in index 3 - 6
print("Data Array: \(arrayInt)")
print("----------")

// Insert data array
arrayInt.insert(234, at: 9) // insert data in index 9
print("Data Array: \(arrayInt)")
print("Amount Data Array Int: \(arrayInt.count)")
print("----------")

// Remove data array in some index
arrayInt.remove(at: 5) // remove data in index 5
print("Data Array: \(arrayInt)")
print("Amount Data Array Int: \(arrayInt.count)")
print("----------")

// Remove data array in last index
arrayInt.removeLast()
print("Data Array: \(arrayInt)")
print("Amount Data Array Int: \(arrayInt.count)")
print("----------")

// Remove data array in first index
arrayInt.removeFirst()
print("Data Array: \(arrayInt)")
print("Amount Data Array Int: \(arrayInt.count)")
print("----------")

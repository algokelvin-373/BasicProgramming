import UIKit

// Type Data: Tuples
var dataTuples01 = ("Machine Learning", "Neural Network")
var (nameTuples, memberTuples) = dataTuples01
print("Name Tuples: \(nameTuples)")
print("Member Tuples: \(memberTuples)")
print()

// Using '_' if the paramter isn't need all
var (nameTuples02, _) = dataTuples01
print("Name Tuples: \(nameTuples02)")
print()

// Tuples with 3 parameter
var dataTuples02 = ("Machine Learning", "Neural Network", "Backpropagation")
var (nameTuples03, memberTuples03, typeTuples03) = dataTuples02
print("Name Tuples: \(nameTuples03)")
print("Member Tuples: \(memberTuples03)")
print("Type Tuples: \(typeTuples03)")

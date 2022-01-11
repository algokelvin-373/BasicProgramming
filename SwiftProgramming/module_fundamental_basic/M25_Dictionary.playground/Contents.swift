import UIKit

var dictionaryData = [Int: String]()
if dictionaryData.isEmpty {
    print("The data dictionaryData is empty")
}
print("Amount dictionaryData = \(dictionaryData.count)")
print("")

// Subscript --> input item dictionary
dictionaryData[2356] = "Swift" //--> Input Data
dictionaryData[4387] = "Kotlin" //--> Input Data
dictionaryData[7687] = "Java" //--> Input Data
dictionaryData[9321] = "Python" //--> Input Data
print("Data dictionaryData = \(dictionaryData)")
print("Amount dictionaryData = \(dictionaryData.count)")

// Replace Data, using 'Subscript' or 'updateValue'
dictionaryData[2356] = "Swift Oke"
dictionaryData.updateValue("Java Joss", forKey: 7687)
print("Data dictionaryData = \(dictionaryData)")
print("Amount dictionaryData = \(dictionaryData.count)")
print("")

// Remove
dictionaryData.removeValue(forKey: 4387)
print("Data dictionaryData = \(dictionaryData)")
print("Amount dictionaryData = \(dictionaryData.count)")

import UIKit

// isEmpty
var data = ""
if data.isEmpty {
    print("The data is empty")
}

// startIndex, endIndex, index
data = "Kelvin"
print(data[data.startIndex])
print(data[data.index(before: data.endIndex)])
print(data[data.index(after: data.startIndex)])
print(data[data.index(data.startIndex, offsetBy: 3)])

// insert
data.insert("-", at: data.endIndex) // insert character --> now data = "Kelvin-"
print(data)
data.insert(contentsOf: "Tandrio", at: data.index(before: data.endIndex)) // insert string --> now data = "KelvinTandrio-"
print(data)
data.insert(contentsOf: "Herwanda", at: data.index(data.startIndex, offsetBy: 6))
print(data)

// remove
data.remove(at: data.index(before: data.endIndex)) // remove character
print(data)
let range = data.index(data.endIndex, offsetBy: -7)..<data.endIndex
data.removeSubrange(range)
print(data)

// append
data.append("!")
print(data)

// count
print(data.count)

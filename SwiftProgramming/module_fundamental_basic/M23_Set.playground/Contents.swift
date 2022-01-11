import UIKit

var setInt: Set<Int> = Set()

// isEmpty and Count
if setInt.isEmpty {
    print("data setInt is empty")
}
print("Amount setInt = \(setInt.count)")
print("----------")

// insert
setInt.insert(20)
print("Data setInt = \(setInt)")
setInt.insert(10)
print("Data setInt = \(setInt)")
setInt.insert(40)
print("Data setInt = \(setInt)")
setInt.insert(25)
print("Data setInt = \(setInt)")
print("Amount setInt = \(setInt.count)")
print("----------")

// remove
setInt.remove(10) // remove data set which value is 10
print("Data setInt = \(setInt)")
setInt.remove(20) // remove data set which value is 10
print("Data setInt = \(setInt)")

// containts
if setInt.contains(40) {
    print("40 is category setInt")
}
else {
    print("40 isn't category setInt")
}
if setInt.contains(10) {
    print("10 is category setInt")
}
else {
    print("10 isn't category setInt")
}

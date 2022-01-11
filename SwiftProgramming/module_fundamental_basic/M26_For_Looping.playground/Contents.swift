import UIKit

// Basic Looping
for index in 1...5 {
   print("\(index) times 3 is \(index * 3)")
}
print("")

// Looping Array Case
print("Looping Array")
let names = ["Kelvin", "Steven", "Linda", "Brigitta"]
for name in names {
   print("Name \(name)")
}
print("")

// Looping Map Case
let cardMember = [3245: "Tony", 9876: "Bruce", 1478: "Steve"]
for (id, name) in cardMember {
   print("\(id) = \(name)")
}
print("")

// Looping Interval
let interval = 6
for i in stride(from: 0, to: 60, by: interval) {
    print("\(i)", terminator: " ")
}
print("")
for i in stride(from: 0, through: 60, by: interval) {
    print("\(i)", terminator: " ")
}

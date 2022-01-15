import UIKit


let dataNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Continue
for i in dataNumber {
    if (i % 2 == 0) {
        continue
    }
    print("\(i)", terminator: ",")
}
print("")

// Break
for j in dataNumber {
    if (j % 2 == 0) && (j % 3 == 0) {
        print("Stop")
        break
    }
    print("\(j)", terminator: ",")
}
print("")

// Fallthrough
let integerToDescribe = 5
var description = "The number \(integerToDescribe) is"
switch integerToDescribe {
    case 2, 3, 5, 7, 11, 13, 17, 19:
       description += " a prime number, and also"
       fallthrough
    default:
       description += " an integer."
}
print(description)
print("")

// Guard ( Early Exit )
func greet(person: [String: String]) {
   guard let name = person["name"] else {
       return
   }
   print("Hello \(name)!")
   guard let location = person["location"] else { // If get conditional false, it's stop here
       print("I hope the weather is nice near you.")
       return
   }
   print("I hope the weather is nice in \(location).")
}
greet(person: ["name": "John"])
greet(person: ["name": "Kelvin", "location": "Palmerah"])

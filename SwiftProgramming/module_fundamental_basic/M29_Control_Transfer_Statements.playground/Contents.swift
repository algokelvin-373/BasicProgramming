import UIKit


let dataNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


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

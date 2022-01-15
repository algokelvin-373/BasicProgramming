import UIKit

enum Planet: String {
   case mercury, venus, earth, mars, jupiter, saturn, uranus, neptune
}

print(Planet.earth.rawValue)

let positionToFind = "uranus"
if let somePlanet = Planet(rawValue: positionToFind) {
   switch somePlanet {
   case .uranus:
       print("Mostly harmless")
   default:
       print("Not a safe place for humans")
   }
} else {
   print("There isn't a planet at position \(positionToFind)")
}

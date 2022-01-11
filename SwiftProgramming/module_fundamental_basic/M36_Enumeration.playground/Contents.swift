import UIKit

// Model Enum type 01
enum CompassPoint {
   case north
   case south
   case east
   case west
}

// Model Enum type 02
enum Planet {
   case mercury, venus, earth, mars, jupiter, saturn, uranus, neptune
}

// Syntax Enum
var callEnumCompass = CompassPoint.west; print(callEnumCompass)
callEnumCompass = .east; print(callEnumCompass)

// with Switch
let callEnumPlanet = Planet.earth
switch callEnumPlanet {
    case .mercury:
        print("You choose \(callEnumPlanet)")
    case .venus:
        print("You choose \(callEnumPlanet)")
    case .earth:
        print("You choose \(callEnumPlanet)")
    default:
        print("You choose other")
}

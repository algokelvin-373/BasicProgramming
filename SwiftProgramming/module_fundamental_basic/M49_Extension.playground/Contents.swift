import UIKit

extension Double {
    // Extension Variable
   var km: Double { return self * 1_000.0 }
   var m: Double { return self }
   var cm: Double { return self / 100.0 }
   var mm: Double { return self / 1_000.0 }
   var ft: Double { return self / 3.28084 }
    
    // Extension Function
    func calculateCircle() -> Double {
        return 3.14 * self * self
    }
}

let fourInch = 50.8.mm
print("4 inch is \(fourInch) meters")

let fourFeet = 4.ft
print("4 feet is \(fourFeet) meters")

let threeCM = 300.cm
print("3 cm is \(threeCM) meters")

let circle = 7.calculateCircle()
print("The area of circle with r: 7 -> \(circle)")

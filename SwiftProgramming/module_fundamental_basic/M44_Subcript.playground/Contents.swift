import UIKit

struct TimesTable {
   let multiplier: Int
   subscript(index: Int) -> Int {
       return multiplier * index
   }
}

let threeTimesTable = TimesTable(multiplier: 3)
print("eight times three is \(threeTimesTable[8])")

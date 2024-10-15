
import Cocoa

var dataArray = [1, 2, 3, 4, 5]
var HalfOpenRange = dataArray.count;

print("Half Open Range Operator = \(HalfOpenRange)")
for i in 0..<HalfOpenRange {
   print("\(i + 1). \(dataArray[i]) ")
}

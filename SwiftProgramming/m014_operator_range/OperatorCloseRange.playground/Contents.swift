
import Cocoa

var ClosedRange = 1...10;
print("Close Range Operator = \(ClosedRange)")
for index in ClosedRange {
    print("\(index)", terminator: " ")
}

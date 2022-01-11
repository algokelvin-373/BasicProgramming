import UIKit

var a: Int? = 12
if (a != nil) {
    print("a is not null, a = \(a!) --> Using '!'")
    print("a is not null, a = \(String(describing: a)) --> Not Using '!'")
}
else {
    print("a is null")
}
print()

var b: Double? = nil
if (b == nil) {
    print("b is null")
}

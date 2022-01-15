import UIKit

// While: Aritmetic
let n = 10
var a = 0
var result01 = 0
while a != n {
    result01 += 4
    print("\(result01) ", terminator: " ")
    a = a + 1
}
print("")

// Repeat While: Geometry
let N = 10
var b = 0
var result02 = 1
repeat {
    result02 *= 2
    print("\(result02) ", terminator: " ")
    b = b + 1
} while b != N
print("\ndone")

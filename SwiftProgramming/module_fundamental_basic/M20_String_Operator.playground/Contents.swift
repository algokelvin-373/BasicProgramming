import UIKit

var StringA = "Kelvin"
var StringB = "Tandrio"

// Using '\()'
print("My name is \(StringA) \(StringB)")

// Using '+'
var StringC = StringA + StringB
print("My name is \(StringC)")

// Using '+='
var StringD = "Herwanda"
var StringE = ""
StringE += StringA
StringE += StringD
StringE += StringB
print("My name is \(StringE)")


import Cocoa

var StringA = "Kelvin"
var StringB = "Tandrio"
var StringC = "Herwanda"

// Using '\()'
print("My name is \(StringA) \(StringB)")

// Using '+'
var StringD = StringA + StringB
print("My name is \(StringD)")

// Using '+='
var StringE = ""
StringE += StringA
StringE += StringC
StringE += StringB
print("My name is \(StringE)")

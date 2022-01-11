import UIKit

func backward(_ s1: String, _ s2: String) -> Bool {
   return s1 > s2
}

let nameProgramming = ["Swift", "Kotlin", "Java", "Python", "Dart"]

// Basic Code Programming
var reserverNameProgram = nameProgramming.sorted(by: backward)
print("Basic Code Programming -> \(reserverNameProgram)")

// Modelling Closure Expression
reserverNameProgram = nameProgramming.sorted(by: { (s1: String, s2: String) -> Bool in
   return s1 > s2
})
print("Modelling Closure Expression -> \(reserverNameProgram)")

// Inferring Type From Context
reserverNameProgram = nameProgramming.sorted(by: { s1, s2 in return s1 > s2 } )
print("Inferring Type From Context -> \(reserverNameProgram)")

// Implicit Returns from Single-Expression Closures
reserverNameProgram = nameProgramming.sorted(by: { s1, s2 in s1 > s2 } )
print("Implicit Returns from Single-Expression Closures -> \(reserverNameProgram)")

// Operator Methods: string-specific
reserverNameProgram = nameProgramming.sorted(by: >)
print("Operator Methods: string-specific -> \(reserverNameProgram)")

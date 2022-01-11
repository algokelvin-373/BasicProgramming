import UIKit

let memberS: Set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let memberA: Set = [3, 5, 6, 8, 9]
let memberB: Set = [1, 3, 4, 6]
let memberC: Set = [3, 4]
print("S = \(memberS)")
print("A = \(memberA)")
print("B = \(memberB)")
print("C = \(memberC)")
print("")

// Intersection
print("Intersection S and A = \(memberS.intersection(memberA))") // without sorted
print("Intersection S and B = \(memberS.intersection(memberB))") // without sorted
print("Intersection A and B = \(memberA.intersection(memberB))") // without sorted
print("Intersection S and A (sorted) = \(memberS.intersection(memberA).sorted())") // with sorted
print("Intersection S and B (sorted) = \(memberS.intersection(memberB).sorted())") // with sorted
print("Intersection A and B (sorted) = \(memberA.intersection(memberB).sorted())") // with sorted
print("")

// Union
print("Union A and B (sorted) = \(memberA.union(memberB).sorted())")
print("")

// SynmetricDifference
print("SynmetricDifference S and A = \(memberS.symmetricDifference(memberA))")
print("SynmetricDifference S and B = \(memberS.symmetricDifference(memberB))")
print("SynmetricDifference A and B = \(memberA.symmetricDifference(memberB))")
print("")

// Substracting
print("Substracting S and A = \(memberS.subtracting(memberA))")
print("Substracting S and B = \(memberS.subtracting(memberB))")
print("Substracting A and B = \(memberA.subtracting(memberB))")
print("Substracting B and A = \(memberB.subtracting(memberA))")
print("")

// isSubset
print("Status memberC isUbset memberB = \(memberC.isSubset(of: memberB))")
print("Status memberC isUbset memberA = \(memberC.isSubset(of: memberA))")

// isSuperset
print("Status memberB isSuperset memberC = \(memberB.isSuperset(of: memberC))")
print("Status memberA isSuperset memberC = \(memberA.isSuperset(of: memberC))")

// isDisjoint
print("Status memberB isDisjoint memberC = \(memberB.isDisjoint(with: memberC))")
print("Status memberA isDisjoint memberC = \(memberA.isDisjoint(with: memberC))")

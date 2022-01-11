import UIKit

/** Variadic Parameters **/
func getData01(_ numbers: Int...) {
    for x in numbers {
        print(x, terminator: " ")
    }
}

/** Function Types as Parameter Types ***/
func printMathResult(_ mathFunction: (Int, Int) -> Int, _ a: Int, _ b: Int) {
   print("Result: \(mathFunction(a, b))")
}
func addTwoInts(_ a: Int, _ b: Int) -> Int { a + b }
func multiplyTwoInts(_ a: Int, _ b: Int) -> Int { a * b }

/** Nested Function ***/
func getData02() {
    func getName() -> String { "kelvin" }
    func getProgram() -> String { "Swift" }
    print(getName())
    print(getProgram())
}

getData01(1, 2, 3, 4, 5)
print("")

printMathResult(addTwoInts, 3, 5)
printMathResult(multiplyTwoInts, 3, 5)

print("")
getData02()


import UIKit

/* Must One Line to Action Code **/
func getData01() -> String {
    "This is function with implicit return"
}

/** Multiple Parameter, return data **/
func getPlusData(a: Int, b: Int) -> Int {
    let result = a + b
    return result
}

/** Multiple Return Data **/
func getData02() -> (program01: String, program02: String) {
    return ("Swift", "Kotlin")
}

/* Tuple Return Types and Multiple Return **/
func getData03(data01: String, data02: String) -> (name01: String, name02: String)? {
    if (data01 == "" || data02 == "") {
        return nil
    }
    return (data01, data02)
}

/* Function without label argumen **/
func getData04(_ name: String) {
    print("Hello \(name), This is function without label argumen")
}

func getData05(name: String = "Kelvin") {
    print("Hello \(name), This is function with default parameter value")
}

print(getData01())

print("5 + 6 = \(getPlusData(a: 5, b: 6))")

let dataReturnMultiple = getData02()
print(dataReturnMultiple.program01+" and "+dataReturnMultiple.program02)

let dataTuplesFunction01 = getData03(data01: "", data02: "")
print((dataTuplesFunction01?.name01 ?? "null")+" and "+(dataTuplesFunction01?.name02 ?? "null"))

let dataTuplesFunction02 = getData03(data01: "Kelvin", data02: "Tandrio")
print((dataTuplesFunction02?.name01 ?? "null")+" and "+(dataTuplesFunction02?.name02 ?? "null"))

getData04("Kelvin")

getData05()
getData05(name: "John")

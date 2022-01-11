import UIKit

var language = "Swift"

// Print general
print(language)

// Print Items
print(10, 20, 30, 40, 50)

// Print Separator
print(10, 20, 30, 40, 50, separator:"....")
print(10, 20, 30, 40, 50, separator:"--")

// Print Terminator
print(1, 2, 3, 4, 5, terminator: "")
print(language, terminator: "")
print()

// Print Separator and Terminator
print(22, 33, 44, 55, separator: "***", terminator: " done")
print()
print("Swift", "Kotlin", "Java", "Python", separator: "<->", terminator: " oke")
print()

// Print variable
print("Your Language \(language)")

import UIKit

// if, if-else, if-else if-else
let number = 50
if (number < 100) {
    print("number is under 100")
}

if (number % 5 == 0) {
    print("\(number) is multiple by 5")
}
else {
    print("\(number) isn't multiple by 5")
}

if (number % 15 == 0) {
    print("\(number) is multiple by 15")
}
else if (number % 20 == 0) {
    print("\(number) is multiple by 20")
}
else {
    print("\(number) isn't multiple by 15 or 20")
}

// switch
let number02 = 2
switch number02 {
    case 1: print("You choose 1")
    case 2: print("You choose 2")
    case 3: print("You choose 3")
    default: print("You choose other")
}

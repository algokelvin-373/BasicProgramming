

import Cocoa

// Break Statement
for j in 1...10 {
    if (j % 2 == 0) && (j % 3 == 0) {
        print("Stop")
        break
    }
    print("\(j)", terminator: " ")
}


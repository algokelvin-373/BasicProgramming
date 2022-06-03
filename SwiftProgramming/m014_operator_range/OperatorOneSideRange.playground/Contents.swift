
import Cocoa

var dataArray2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

var OneSideRange01 = dataArray2[...4];
print("One Range index from 0 - 4 = \(OneSideRange01)")

var OneSideRange02 = dataArray2[4...];
print("One Range index from 4 - 9 = \(OneSideRange02)")

var OneSideRange03 = dataArray2[..<4];
print("One Range index < 4 = \(OneSideRange03)")

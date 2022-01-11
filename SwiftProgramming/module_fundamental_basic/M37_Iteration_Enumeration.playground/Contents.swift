import UIKit

enum Food: CaseIterable {
    case bread
    case cake
    case pizza
    case pasta
}

print("Amount Food : \(Food.allCases.count)")
for data in Food.allCases {
    print(data)
}

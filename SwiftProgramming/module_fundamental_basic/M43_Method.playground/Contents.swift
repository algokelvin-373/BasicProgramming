import UIKit

class Counter {
    var count = 0
    func increment() {
        count+=1
    }
    
    func incrementBy(amount: Int) {
        count += amount
    }
 
    func reset() {
        count = 0
    }
}

let counter = Counter()
 
counter.increment();
print("Count = \(counter.count)")

counter.incrementBy(amount: 5);
print("Count = \(counter.count)")

counter.reset();
print("Count = \(counter.count)")

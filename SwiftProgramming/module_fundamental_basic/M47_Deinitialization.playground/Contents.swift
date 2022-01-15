import UIKit

var counter = 3
class baseClass {
   init() {
      counter+=1
   }
   deinit {
      counter-=1
   }
}

// Statement when call 'nil', it mean deinit called
var baseOne: baseClass? = baseClass()
print(counter)
baseOne = nil // deinit called
print(counter)

print(counter)
baseOne = nil // deinit called
print(counter) // it's not change because deinit just one time called

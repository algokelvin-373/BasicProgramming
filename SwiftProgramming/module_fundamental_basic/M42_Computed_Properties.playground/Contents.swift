import UIKit

struct Point {
  var x = 0.0, y = 0.0
}
 
struct Shape {
  var origin = Point()
  var center: Point {
    get {
     return Point(x: origin.x/2, y: origin.y/2)
    }
    set {
     origin.x = newValue.x/2
     origin.y = newValue.y/2
    }
 }
}

var shape = Shape(origin: Point())
shape.origin.x = 30
shape.origin.y = 60
print("The center is = \(shape.center)")

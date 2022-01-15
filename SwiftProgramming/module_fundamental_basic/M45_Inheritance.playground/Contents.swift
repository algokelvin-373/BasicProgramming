import UIKit

// Parent Class
class Vehicle {
   var currentSpeed = 0.0
   var description: String {
       return "traveling at \(currentSpeed) miles per hour"
   }
 
    func makeNoise(song: String) {
        print("This is method makeNoise in Vehicle class -> \(song)")
    }
}

// Without Overriding
class Bicycle: Vehicle {
   var hasBasket = false
}

// With Overriding Function
class Train: Vehicle {
    override func makeNoise(song: String) {
        print(super.makeNoise(song: "Wkwkwk...")) // This is call print in class Vehicle
        print(song)
   }
}

// With Overriding Variable
class Car: Vehicle {
   var gear = 1
   override var description: String {
       return super.description + " in gear \(gear)"
   }
}

let bicycle = Bicycle()
bicycle.hasBasket = true
bicycle.currentSpeed = 15.0
print("Bicycle: \(bicycle.description)")

let train = Train()
train.makeNoise(song: "Choo Choo")

let car = Car()
car.currentSpeed = 25.0
car.gear = 3
print("Car: \(car.description)")

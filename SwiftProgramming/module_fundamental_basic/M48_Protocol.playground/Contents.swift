import UIKit

protocol FullyNamed {
   var fullName: String { get }
}

protocol NickNamed {
    var nickName: String { get }
}


// looks like Interface in Java Kotlin
struct Person: FullyNamed, NickNamed {
    var fullName: String
    var nickName: String
}

let person = Person(fullName: "Kelvin Herwanda Tandrio", nickName: "Kelvin")
print(person.fullName)
print(person.nickName)

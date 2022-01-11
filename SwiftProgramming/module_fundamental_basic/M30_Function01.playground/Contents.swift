import UIKit

func getMessage01(){
    print("This is Basic Function")
}

func getMessage02(message: String) {
    print(message)
}

func getMessage03() -> String {
    return "This is function with return data"
}

func getMessage04(name: String) -> String {
    return "Hello \(name), this is function with parameter and return data"
}

getMessage01()
getMessage02(message: "This is function with parameter")
print(getMessage03())
print(getMessage04(name: "Kelvin"))

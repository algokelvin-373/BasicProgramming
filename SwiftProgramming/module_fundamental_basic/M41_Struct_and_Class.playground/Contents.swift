import UIKit

struct Resolution {
   var width = 0
   var height = 0
}
 
class ImageMode {
   var resolution = Resolution()
   var interlaced = false
   var name: String?
}


// Structure and Class Instances
let structResolution = Resolution()
let classImageMode = ImageMode()

// Accessing Properties && Classe Are Reference Type
classImageMode.name = "Kelvin Tandrio"
classImageMode.resolution.width = 720
classImageMode.resolution.height = 360
print("The name of image = \(String(describing: classImageMode.name))")
print("The width of image (from struct) = \(structResolution.width)")
print("The width of image (from class) = \(classImageMode.resolution.width)")
print("The height of image (from class) = \(classImageMode.resolution.width)")

// Memberwise Initializers for Structure Types
let resolutionDefault = Resolution(width: 640, height: 320)
print("The width of image (from struct) = \(resolutionDefault.width)")
print("The height of image (from struct) = \(resolutionDefault.height)")

import UIKit

// One init
struct Fahrenheit {
   var temperature: Double
   init() {
       temperature = 32.0
   }
}

var f = Fahrenheit()
print("The default temperature is \(f.temperature)° Fahrenheit")


// Two init
struct Celsius {
   var temperatureInCelsius: Double
   init(fromFahrenheit fahrenheit: Double) {
       temperatureInCelsius = (fahrenheit - 32.0) / 1.8
   }
   init(fromKelvin kelvin: Double) {
       temperatureInCelsius = kelvin - 273.15
   }
}
let fromFahrenheitToCelcius = Celsius(fromFahrenheit: 122.0)
let fromKelvinToCelcius = Celsius(fromKelvin: 300.15)
print(fromFahrenheitToCelcius.temperatureInCelsius)
print(fromKelvinToCelcius.temperatureInCelsius)

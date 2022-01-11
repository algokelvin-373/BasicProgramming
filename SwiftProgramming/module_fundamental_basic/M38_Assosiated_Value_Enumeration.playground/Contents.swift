import UIKit

enum Barcode {
   case upc(Int, Int, Int, Int)
   case qrCode(String)
}

var barcodeQRCode = Barcode.qrCode("Kelvin Tandrio")
print(barcodeQRCode.self)
barcodeQRCode = .qrCode("Swift Programming")
print(barcodeQRCode.self)

switch barcodeQRCode {
case .upc(let numberSystem, let manufacturer, let product, let check):
   print("UPC: \(numberSystem), \(manufacturer), \(product), \(check).")
case .qrCode(let productCode):
   print("QR code: \(productCode).")
}

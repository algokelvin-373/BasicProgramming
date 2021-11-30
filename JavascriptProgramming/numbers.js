let x = 123
let y = 3.143

document.getElementById('toString').innerHTML = x.toString()
document.getElementById('toExp2').innerHTML = y.toExponential(2)
document.getElementById('toExp4').innerHTML = y.toExponential(4)
document.getElementById('toFixed2').innerHTML = y.toFixed(2)
document.getElementById('toFixed4').innerHTML = y.toFixed(4)
document.getElementById('toPrec2').innerHTML = y.toPrecision(2)
document.getElementById('toPrec4').innerHTML = y.toPrecision(4)
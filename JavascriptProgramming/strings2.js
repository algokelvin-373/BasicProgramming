let data = "AlgoKelvin Learn Java";

document.getElementById('substr').innerHTML = data.substr(5,10)
document.getElementById('substr_negative').innerHTML = data.substr(-10, -5)
document.getElementById('substr_end').innerHTML = data.substr(5)
document.getElementById('substr_negative_end').innerHTML = data.substr(-10)

document.getElementById('replace').innerHTML = data.replace("Java", "Javascript")
document.getElementById('upper').innerHTML = data.toUpperCase()
document.getElementById('lower').innerHTML = data.toLowerCase()
document.getElementById('trim').innerHTML = data.trim()

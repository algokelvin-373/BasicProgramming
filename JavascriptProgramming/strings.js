let data = "AlgoKelvin Learn Javascript";

document.getElementById('slice').innerHTML = data.slice(5,10)
document.getElementById('slice_negative').innerHTML = data.slice(-10, -5)
document.getElementById('slice_end').innerHTML = data.slice(5)
document.getElementById('slice_negative_end').innerHTML = data.slice(-10)

document.getElementById('substring').innerHTML = data.substring(5,10)
document.getElementById('substring_negative').innerHTML = data.substring(-10, -5)
document.getElementById('substring_end').innerHTML = data.substring(5)
document.getElementById('substring_negative_end').innerHTML = data.substring(-10)

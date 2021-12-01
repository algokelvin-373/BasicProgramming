const y = ["Java", "Kotlin", "PHP", "Javascript"]

y.splice(1, 0, "HTML, CSS") // position = 1, delete = 0
document.getElementById('splice1').innerHTML = y

y.splice(2, 3, "Dart", "Python") // position = 2. delete = 3
document.getElementById('splice2').innerHTML = y

y.splice(0,1) // position = 0, delete = 1
document.getElementById('splice3').innerHTML = y
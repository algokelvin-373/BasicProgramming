const x = ["Java", "HTML", "CSS", "Javascript"]

x.push("Kotlin")
document.getElementById('push').innerHTML = x

x.pop()
document.getElementById('pop').innerHTML = x

x.shift()
document.getElementById('shift').innerHTML = x

x.unshift("PHP")
document.getElementById('unshift').innerHTML = x

x[2] = "Python"
document.getElementById('add2').innerHTML = x

delete x[1]
document.getElementById('delete1').innerHTML = x
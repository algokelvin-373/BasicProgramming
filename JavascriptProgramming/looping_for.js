const codes = ["Javascript", "Java", "Kotlin", "Python", "Dart", "Switch"];

let text = "";
for (let i = 0; i < codes.length; i++) {
  text += codes[i] + "<br>";
}

document.getElementById("coding").innerHTML = text;
const codes = ["Javascript", "Java", "Kotlin"];

let text = "";
for (let x of codes) {
  text += x + "<br>";
}
document.getElementById("codes").innerHTML = text;

const channel = "AlgoKelvin";
let txt = ""
for (let x of channel) {
    txt += x + " ";
}
document.getElementById("arraystr").innerHTML = txt;
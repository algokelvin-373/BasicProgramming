const person = {
    fname:"Kelvin", 
    lname:"Tandrio", 
    age:26
}; 

let txt = "";
for (let x in person) {
  txt += person[x] + " ";
}

document.getElementById("person").innerHTML = txt;

const numbers = [10, 20, 30, 40, 50];

let num = "";
for (let x in numbers) {
  num += numbers[x] + " ";
}

document.getElementById("number").innerHTML = num;
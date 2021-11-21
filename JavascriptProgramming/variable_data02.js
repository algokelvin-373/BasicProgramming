function showResultLet() {
    let x = 5;
    document.getElementById("before_let").innerHTML = "Before x : "+ x;
    x = 10;
    document.getElementById("after_let").innerHTML = "After x  : "+ x;
    // let x = 373; -> Error: Identifier 'x' has already been declared

    let y = 373;
    document.getElementById("again_let").innerHTML = "Value y  : "+ y;
}
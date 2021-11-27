function Logical() {
    let a = true;
    let b = false;

    // Logical AND
    document.getElementById('and1').innerHTML = a && a;
    document.getElementById('and2').innerHTML = a && b;
    document.getElementById('and3').innerHTML = b && a;
    document.getElementById('and4').innerHTML = b && b;

    // Logical OR
    document.getElementById('or1').innerHTML = a || a;
    document.getElementById('or2').innerHTML = a || b;
    document.getElementById('or3').innerHTML = b || a;
    document.getElementById('or4').innerHTML = b || b;

    // Logical NOT
    document.getElementById('not1').innerHTML = !a;
    document.getElementById('not2').innerHTML = !b;
}
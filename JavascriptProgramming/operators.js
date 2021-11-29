function arithmetic() {
    let x = 5;
    let y = 2;

    document.getElementById('plus').innerHTML = x + y;
    document.getElementById('minus').innerHTML = x - y;
    document.getElementById('times').innerHTML = x * y;
    document.getElementById('divided').innerHTML = x / y;
    document.getElementById('module').innerHTML = x % y;
    document.getElementById('exponen').innerHTML = x ** y;
}
function assign() {
    let a = 13;
    let x = 1, y = 2;

    document.getElementById('assign1').innerHTML = (a += x) + ', now a = ' + a;
    document.getElementById('assign2').innerHTML = (a -= x) + ', now a = ' + a;
    document.getElementById('assign3').innerHTML = (a *= y) + ', now a = ' + a;
    document.getElementById('assign4').innerHTML = (a /= y) + ', now a = ' + a;
    document.getElementById('assign5').innerHTML = (a %= y) + ', now a = ' + a;
    document.getElementById('assign6').innerHTML = (a **= y) + ', now a = ' + a;
}

function assign2() {
    let a = 20;
    let x = 10;

    document.getElementById('assignX').innerHTML = (a += x) + ', now a = ' + a;
}
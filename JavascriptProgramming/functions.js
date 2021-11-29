// Function without params and return
function func1() {
    document.getElementById('func1').innerHTML = 'AlgoKelvin 1'
}

// Function with param, without return
function func2(msg) {
    document.getElementById('func2').innerHTML = msg
}

// Function without param, with return
function func3() {
    return 'AlgoKelvin 3'
}

// Function with param and return
function func4(msg) {
    return msg
}

func1()
func2('AlgoKelvin 2')
document.getElementById('func3').innerHTML = func3()
document.getElementById('func4').innerHTML = func4('AlgoKelvin 4')
function IfElse(x) {
    var msg
    if (x > 0) {
        msg = x + " is positive"
    } else {
        msg = x + " is negative"
    }
    return msg
}

const x = 10
const y = -10

const msgX = IfElse(x)
const msgY = IfElse(y)

document.getElementById('ifElse1').innerHTML = msgX
document.getElementById('ifElse2').innerHTML = msgY

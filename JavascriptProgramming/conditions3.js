function MultiConditions(x) {
    var msg
    if (x > 0) {
        msg = x + " is positive"
    } else if (x == 0) {
        msg = x + " is zero"
    } else {
        msg = x + " is negative"
    }
    return msg
}

const x = 10
const y = 0
const z = -10

const msgX = MultiConditions(x)
const msgY = MultiConditions(y)
const msgZ = MultiConditions(z)

document.getElementById('multiCondition1').innerHTML = msgX
document.getElementById('multiCondition2').innerHTML = msgY
document.getElementById('multiCondition3').innerHTML = msgZ

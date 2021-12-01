function SingleIf(x) {
    var msg = "$x is negative"
    if (x > 0) {
        msg = "$x is positive"
    }
    return msg
}

const x = 10
const y = -10

const msgX = SingleIf(x)
const msgY = SingleIf(y)

document.getElementById('singleIf1').innerHTML = msgX
document.getElementById('singleIf2').innerHTML = msgY

function Mail2() {
    this.from = 'kelvintandrio@algokelvin.com'
    this.contact = []
    this.dataMsg = "AlgoKelvin"
};
   
Mail2.prototype.sendMessage = function(msg, to) {
    let msg2 = `You send: ${msg} to ${to} from ${this.from}`
    console.log(msg2)
    this.contact.push(to)
    document.getElementById("oop").innerHTML = this.contact
};

const mail2 = new Mail2();
mail2.sendMessage('Hello, Elisabeth', 'sabethrwh@algokelvin.com');
mail2.sendMessage('Hello, Kurnia', 'kurnia@algokelvin.com');
mail2.sendMessage('Hello, Andryaas', 'andryaas@algokelvin.com');

document.getElementById("dt").innerHTML = mail2.dataMsg

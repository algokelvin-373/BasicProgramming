function Mail() {
    this.from = 'kelvintandrio@algokelvin.com';
};
   
Mail.prototype.sendMessage = function(msg, to) {
    let msg2 = `You send: ${msg} to ${to} from ${this.from}`;
    console.log(msg2);
    document.getElementById("oop").innerHTML = msg2
};

const mail1 = new Mail();
mail1.sendMessage('Hello, Elisa', 'elisarwh@algokelvin.com');

class Animal {
    //private variable
    #nameAnimal 

    constructor(name) {
        this.#nameAnimal = name
    }
    
    show() {
        return this.#nameAnimal
    }
}

let animal = new Animal("mouse")
document.getElementById("anim").innerHTML = animal.show()


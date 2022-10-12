class Person {
    constructor(name, job) {
        this.name = name
        this.job = job
    }
    showProfile() {
        document.getElementById("all").innerHTML = " - This - " + this.job
    }
}

class Developer extends Person {
    // Overriding Property
    constructor(develop, name, job) {
        super(name, job)
        this.develop = develop
    }
    // Overriding Method
    show() {
        super.showProfile()
    }
}

let develop = new Developer("Android", "Kelvin Tandrio", "Software Developer")
document.getElementById("name").innerHTML = develop.name
document.getElementById("job").innerHTML = develop.job
document.getElementById("dev").innerHTML = develop.develop
develop.show()

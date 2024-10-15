class Person {
    constructor(name, job) {
        this.name = name
        this.job = job
    }
}

let person = new Person("Kelvin Tandrio", "Android Developer")
document.getElementById("name").innerHTML = person.name
document.getElementById("job").innerHTML = person.job

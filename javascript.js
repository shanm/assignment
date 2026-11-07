console.log("Hello")
let name = "shan"
name = "raja"
console.log(name)

function add(a, b) {
    return a + b
}

//let result = add(2, 5)
console.log(add(2, 5))

function greet(name) {
    console.log('Hello, ${name}!');
    //return 'Hello, ${name}!'
}

greet("kkkkk")

let name_wel = () => "Welcome Shanmuga"
console.log(name_wel())

let global_var = "I'm global variale"

function outerFunction() {
    let outer_var = "I'm a outer funtion"
    function innerFunction() {
        let inner_var = "I'm a inner function"
        console.log(inner_var)
        console.log(outer_var)
        console.log(global_var)
    }
    return innerFunction
}

const closure = outerFunction();
closure()

////////////

let arr = [1,2,3]
console.log(arr)


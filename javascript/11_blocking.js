function a() {
    console.log('a')
}

console.log('hi')   // 1.
setTimeout(a, 3000)  // 3.
console.log('bye') // 2.


function printHello() {
    console.log('Helloooo')
}

function baz() {
    console.log('baz') // 1
    setTimeout(printHello, 0) // 3
    console.log('baz end') // 2
}


function bar() {
    console.log('bar')
    baz()
}

function foo() {
    console.log('foo')
    bar()
}

foo()
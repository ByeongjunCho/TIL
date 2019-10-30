var myVar // 선언
myVar = 1 // 할당
colsol.log(myVar)

var myVar = 'Hello' // 재선언 가능


let myLet  
myLet = 2  
myLet = 3  // 재할당 가능
let myLet = 'hi'  // SyntaxError -> 이미 선언됨(error) 재선언 불가능


// const myConst // SyntaxError -> 초기화 누락(선언과 할당이 필요하다)
const myConst = 'hi' // 선언과 동시에 할당이 필요
// myConst = 'bye' // TypeError -> const에 할당함(재할당 불가능)


/* 
    1-2. scope
*/

let VarFunction = function() {
    var myVar = 0
    if (true) {
        var myVar = 1
        console.log(myVar)
    }
    console.log(myVar)
}

let LetFunction = function() {
    let myLet = 0
    if (true) {
        let myLet = 1
        console.log(myLet)
    }
    console.log(myLet)
}
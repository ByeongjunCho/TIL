console.log('Happy!')

// var
var name = '변수'
console.log(name)

console.log(a)  // undefined
var a = '에이'
// 변수 hoisting(호이스팅)
// : 변수의 선언을 해당 스코프 범위 내에서 최상단에 변수의 선언을 함.
// var a
// console.log(a)
// a = '변수'

// let(ES6+)
console.log(b)  // Error : Reference error
let b = '변수'
b = '다른변수'  // 재할당 가능
let b = '다른변수'  // 재선언 불가능

// const (ES6+)
// 재선언 및 재할당이 불가능하다.

const c = '상수' 
c = '다른값'  // 재할당
const c = '다른상수' // 재선언
const tak  // 선언만 할 수 없음(선언과 동시에 할당이 필요함)

// let, const vs var
// 재선언이 불가능하다. vs 가능하다
// 블록 스코프 vs 함수 스코프
var outerVar = '밖'
if (true){
    var outerVar = '안' // 안
    console.log(outerVar)
}
console.log(outerVar)  // 안

let outerLet = '밖'
if(true){
    let outerLet = '안'
    console.log(outerLet)  // 안
}
console.log(outerLet)  // 밖
# javascript

## 1. 기초

### 1. var

```javascript
var myVar // 선언
myVar = 1 // 할당
colsol.log(myVar)

var myVar = 'Hello' // 재선언 가능
```

### 2. let

```javascript
let myLet  
myLet = 2  
myLet = 3  // 재할당 가능
let myLet = 'hi'  // SyntaxError -> 이미 선언됨(error) 재선언 불가능
```

### 3. const

```javascript
// const myConst // SyntaxError -> 초기화 누락(선언과 할당이 필요하다)
const myConst = 'hi' // 선언과 동시에 할당이 필요
// myConst = 'bye' // TypeError -> const에 할당함(재할당 불가능)
```

### 4. scope관련

```javascript
let VarFunction = function() {
    var myVar = 0
    if (true) {
        var myVar = 1
        console.log(myVar) // 1
    }
    console.log(myVar) // 1
}
```

* var는 함수 스코프로 모두 1이 출력된다

```javascript
let LetFunction = function() {
    let myLet = 0
    if (true) {
        let myLet = 1
        console.log(myLet) // 1
    }
    console.log(myLet) // 0
}
```

* let과 const는 블록 스코프로 지역변수와 비슷한 형식을 따른다.

### 5. hoisting

```javascript
console.log(taewoo)  // undefined
var taewoo = '김태우'

/*
var taewoo
consol.log(taewoo)
taewoo = '김태우'
*/
```

* var 형식은 hoisting이 되어 선언 전에 접근이 가능하다.

```javascript
console.log(kyungho)  // ReferenceError - 초기화하기전 접근 X
let kyungho = '이경호'
```

* let 형식은 초기화전에 접근이 불가능하다.

```
var형식
1. 선언과 동시에 초기화
2. 할당

let, const는 TDZ(Temporal Dead Zone)이 존재
1. 선언
2. TDZ
3. 초기화
4. 할당
```

### 6. type

```
* 원시타입(primitive data type)
    - boolean
    - null
    - undefined
    - number
    - string
    - symbol (ES6+)
```

* number

```javascript
3
-5
3.14
2.14e4
2.14e-4
Infinity
NaN  // Not a Number
0/0  // NaN
10/0 // Infinity
```

* string

```javascript
// string
let myName = '탁희'
myName = "탁\n희"
// `(backtick) : ES6+ 템플릿리터럴
// string interpolation, 줄바꿈(개행)
myName = `탁

희`
console.log(`안녕하세요, ${myName}입니다.`)
```

* boolean

```javascript
true
false
```

* empty value

```javascript
undefined // type -> undefined
null // type -> object
typeof null
typeof undefined
```

### 7. 연산자(operator)

```javascript
// 동등 연산자(==)
// 강제 형변환을 하면서 비교

1 == '1' // true

// 일치 연산자(===)
1 === '1' // false

// 할당( =, +=, -=, *=, /=)

// 비교 >, <, >=, <=

// 논리 and(&&) or(||)

// not !

// 삼항연산자  표현식 ? true:false
```

## 2. 조건문, 반복문

### 1. 조건문

* 기본구조

```javascript
if (조건1) {
    실행문1
} else if (조건2) {
    실행문2
}
else {
    실행문3
}
```

```javascript
// 예제
let userName = prompt('넌 누구니?')
let message

if (userName === 'ssafy') {
    message = '<h1>Hello SSAFY</h1>'
} else if (userName == '1q2w3e4r') {
    message = '<h1>Admin page입니다.</h1>'
} else {
    message = `<h1>${userName} 환영합니다. </h1>`
}
document.write(message)
```

* if문은 조건에 해당하면 함수를 실행하고 if문이 끝난다.

### 2. switch - case

```javascript
switch(입력조건) {
    case 조건1: {
        실행문1
        break
    }
    case 조건2: {
        실행문2
        break
    }
    default: {
        실행문3
    }
}
```

* switch문에서는 break가 없으면 default가 실행되기 때문에 break가 필요하다.

```javascript
// 예제
switch(userName) {
    case '1q2w3e4r': {
        message = '<h2> 관리자님 충성충성 </h2>'
        break
    }
    case 'ssafy': {
        message = '<a href="https://edu.ssafy.com">싸피</a>'
        break
    }
    default: {
        message = `<h1>${userName} 환영합니다. </h1>`
    }
}

document.write(message)
```

### 3. while

```javascript
while (조건) {
    실행문
}
```

### 4. for

```javascript
/*
    * 반복문
    var는 함수스코프를 가지고 있어서 for문 이후에 i 변수값이 유지
    let은 블록스코프를 가지고 있어서 for문 이후에 해당 변수는 없음
*/

for (let i=0; i<N; i++) {
    실행문
}

for (var i=0; i<3; i++) {
    console.log(i)
}
console.log(i)
// 0 1 2 3 출력
for (let j=0; j<3; j++) {
    console.log(j)
} 
// 0 1 2 출력
console.log(j)  // RefereneError
```

```javascript
let myArray = ['태', '경', '은']
for (let name of myArray) {
    document.write(name)
}
```

* python과 비슷하게 배열의 내용을 하나씩 가지고 와서 사용할 수 있다.

## 3. 함수

### 1. 함수선언

* 함수선언은 두가지 방식이 있다.

```javascript
console.log(myAdd(1, 2))
console.log(myAdd2(1, 2)) // Error

// 선언식 -> hoisting
function myAdd(a, b){
    return a + b
}

// 표현식
let myAdd2 = function (a, b) {
    return a + b
}
```

* 선언식은 hoisting이 된다.

### 2. Arrow함수

* ES6+ 이상에서 사용 가능하다.

```javascript
// 1. function 키워드 삭제 후 =>
let myArrowFunction = (a) => {return a+1}
// 1-1. 인자가 하나라면, 소괄호 삭제 가능
// 1-2. 문장이 한 줄이고, 리턴이라면 중괄호 및 return 키워드 생략 가능
let myArrowFunction1 = a => a + 1

myArrowFunction(1) // 2출력
myArrowFunction1(1) // 2출력

let greeting = function() {
    console.log('happy!')
}

// 1-3. 인자가 없는 경우에는 () or _
greeting = () => {console.log('happy!')}
greeting = _ => {console.log('happy!')}

// 1-4. 기본인자
let greeting2 = (name='타기') => name

// 익명함수
(function(a) {
    return a * 10
}(100))

((a) => a*10(10))
```

## 4. Array

### 1. Array 기본

```javascript
let numbers = [10, 1, 3, 5]

numbers[0] // 10
numbers[-1] // undefined
numbers.length // 4

numbers.reverse() // return + 원본 변경

numbers.push(3) // 마지막 원소에 추가 + return (길이)
numbers.pop() // 마지막 원소 제거 + return (해당 원소)
numbers.unshift(3) // 가장 첫번째 원소에 추가 + return (길이)
numbers.shift() // 가장 첫번째 원소 제거 + return(원소)

numbers.includes(1) // 포함 여부 확인
numbers.includes(10000) // false return
numbers.indexOf(1) // 가장 먼저 존재하는 위치 반환

numbers.join() // 기본
numbers.join('-') // -로 연결
```

### 2. Array method

```javascript
/*
    Array helper methods
*/ 

/*
    Array.forEach
*/
let numbers = [1,2,3]
// 1. 반복문 (for)
for (let i=0; i<numbers.length; i++) {
    console.log(numbers[i])
}

// 2. 반복문 (for ... of)

for(let v of numbers) {
    console.log(v)
}

// 3. forEach -> return 없음
numbers.forEach(function(num){
    console.log(num)
})

// 실습
const images = [
    {height: 30, width: 20},
    {height: 100, width: 100},
    {height: 10, width: 5}
]

let areas = []
images.forEach(function(image, idx){
    console.log(idx)
    areas.push(image.height * image.width)
})

console.log(areas)

/*
    map : 콜백함수의 return 결과를 각각 원소로 하는 배열을 **리턴**
*/

let numbers = [1,2,3]

let doubleNumbers = numbers.map(function(number){
    return number * 2
})
console.log(doubleNumbers)

let doubleNumbers2 = numbers.map( number => number*2)
console.log(doubleNumbers2)

// 실습 images -> map
let areas = images.map(images => images.height * images.width)
let areas = images.map(function(image){
    return image.height * image.width
})

/*
    filter: 콜백함수의 return 결과가 참인 것을 각각 원소로 하는 배열을 **리턴**
*/
// images의 높이가 100보다 작은 object만 담은 배열
let myImage = []
for (let image of images){
    if (image.height < 100){
        myImage.push(image)
    }
}
console.log(myImage)
myImage = images.filter(function(image){
    return image.height < 100
})
console.log(myImage)


// fruit 만 뽑아내기
let products = [
    {name: 'banana', type:'fruit'},
    {name: 'tomato', type:'vegetable'},
    {name: 'apple', type:'fruit'},
    {name: 'cucumber', type:'vegetable'},
]

let bag = []
products.filter(product => product.type === 'vegetable')
products.filter(function(product){return product.type === 'vegetable'})


/*
    reduce(callbackfn, initialvalue): return 결과를 누적한 결과를 return
*/

let mySsafy = [100, 100, 95, 90]
let totalScore = mySsafy.reduce(function(total,score){
    console.log(score) // 원소
    console.log(total) // 누적
    return total + score
}, 100) // 초기값
mySsafy.reduce((total, score) => total+score, 100)

/*
    find : 일치하는 첫번째 원소를 리턴
*/
mySsafy.find(function(score){
    return score === 2
})

let heros = [
    {name: '헐크', age: 100},
    {name: '아이언맨', age: 50},
    {name: '스파이더맨', age: 30}
]

// 나이가 30인 사람
heros.find(function(a){
    return a.age === 30
})
heros.find(hero => hero.age === 30)

/*
    some: 원소 중 하나라도 조건에 부합하면 true
    every: 모든 원소가 조건에 부합하면 true
*/

let myNumbers = [1,2,3,4]
myNumbers.some(function(number){
    return number % 2 === 0
})
myNumbers = [3, 5]
myNumbers.some(function(number){
    return number % 2 === 0
})
myNumbers.every(function(number){
    return number % 2 !== 0
})
```



## 5. Object

```javascript
const me = {
    // 프로퍼티
    name: 'kim',
    'phone number': '0102345678',
    phone: {
        type: 'iphone XS MAX'
    },
    // 메서드 function 키워드만 작성하자!
    greeting: function() {
        console.log(`hi ${this.name}`)
    },
    greeting2: () => {
        console.log(this) // 전역객체 window
        console.log(`hi ${this.name}`)
    } // Arror function은 사용할 수 없다.
}

console(me.name)
console(me['name'])
console(me.phone.type)

// ES6+ 오브젝트 리터럴
let book = '자바스크립트 완전 정복'
let albums = {
    IU: ['좋은날', '밤편지'],
    BTS: ['작은것들을 위한 시']
}

let bag = {
    book,
    albums
} // bag는 book와 albums를 가진 objects가 된다.

// JSON (javascript object notation - 자바스크립트 오브젝트 표기법) 
// 문자열
// object -> JSON
let jsonData = JSON.stringify(me)
let myObject = JSON.parse(jsonData)
```

* 모든 `var`변수는 window method로 불러올 수 있다.

```javascript
var a = 1
var b = 3
window.a  // 1
window.b  // 3
```

## 6. DOM 조작(Document Object Model)

```javascript
document.querySelector('#__id__')  // id를 기준으로 선택
document.querySelector('.__class__')  // class로 선택
document.querySelector('HTML tag')  // tag로 선택
ul = document.querySelector('#my-list')
ul.childeren // 자식 선택
ul.previousElementSibling // 이전의 형제값 선택
ul.attributes // 속성 접근
```

* 다양한 방법으로 조작이 가능하다.

```javascript
const newDino = document.createElement('img') // image tag 생성
newDino.alt = '공룡'
newDino.src = "https://is4-ssl.mzstatic.com/image/thumb/Purple118/v4/88/e5/36/88e536d4-8a08-7c3b-ad29-c4e5dabc9f45/AppIcon-1x_U007emarketing-sRGB-85-220-0-6.png/246x0w.jpg"
newDino.id = 'new-dino'
newDino.height = 100
newDino.width = 100
newDino.style.width = "100px"
```

* 새로운 tag 생성

```javascript
bg.appendChild(newDino)
```

* 만든 tag를 기존의 값에 입력


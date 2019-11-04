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

### 1. object 생성

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

### 2. 함수를 이용한 object 생성(생성자 함수)

```javascript
// object 함수 구현
const Person = function(name, phone){
    this.name = name
    this.phone = phone
    this.greeting = function(){
        return 'hi, ' + this.name
    }
}

const ho = new Person('u', '123-456-7890')

// 생성자 함수에서는 arrow function 사용 금지
const Animal = name => {
    this.name = name
}
```

### 3. object 리터럴 이용

```javascript
const name = 'nugu'
const phone = '010-1234-1324'
const greeting = function() {
    return 'hi ,' + this.name
}
const you = {
    name,
    phone,
    greeting
}
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

### 1. 버튼 생성 예제

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>

<body>
  <h1>Todo List</h1>
  <h1>
    <div id="time"></div>
  </h1>
  <form action="" id="form">
    <label for="input">할 일을 입력하세요</label>
    <input type="text" id="input">
    <button id="input-button" type="submit">+</button>
  </form>
  <ul id="todo-list">
    <li> +버튼이 눌리면 리스트에 추가되도록 구현하세요. </li>
  </ul>

  <script>
    const form = document.querySelector('#form')
    const input = document.querySelector('#input')
    const button = document.querySelector('#input-button')
    const todos = document.querySelector('#todo-list')
    button.addEventListener('click', function (event) {
      // const input = event.target.previousElementSibling // 이벤트가 발생한 대상
      if (input.value) { // 예외 처리 - #input에 데이터가 있다면
        event.preventDefault() // form tag의 action을 disable
        // li 하나를 만들어서
        const li = document.createElement('li')
        // 값을 넣고
        console.log(this.previousElementSibling) // 이벤트가 발생한 대상
        const deleteButton = document.createElement('button') // 삭제버튼 생성
        deleteButton.style.marginLeft = '10px'  
        deleteButton.innerText = '삭제'
        // todo-list에 붙인다.
        li.innerText = input.value + document.getElementById('#time')
        li.appendChild(deleteButton) // deleteButton 추가
        deleteButton.addEventListener('click', function (event) { // deleteButton에 대한 이벤트
          li.remove()
        })

        input.value = ''

        // li.innerText = document.getElementById('input').value
        // document.getElementById('input').value = ""
        todos.appendChild(li)

        // 삭제버튼 이벤트

      } else {
        alert('내용을 입력하세요')
      }
    })

    function checkTime(i) {
      if (i < 10) {
        i = "0" + i;
      }
      return i;
    }

    function startTime() {
      var today = new Date();
      var h = today.getHours();
      var m = today.getMinutes();
      var s = today.getSeconds();
      // add a zero in front of numbers<10
      m = checkTime(m);
      s = checkTime(s);
      document.getElementById('time').innerHTML = h + ":" + m + ":" + s;
      t = setTimeout(function () {
        startTime()
      }, 500);
    }
    startTime();
  </script>
</body>
</html>
```



## 7. Javascript 실행구조

* 이벤트 루프 : call stack, callback queue 확인
  * call stack이 비어있으면, callback queue에서 call stack으로 이동
  * 이벤트(함수실행...)
  * tick(틱)
* synchronous/Asynchronous
* blocking/non-blocking

```javascript
function a() {
    console.log('a')
}

console.log('hi')   // 1.
setTimeout(a, 3000)  // 3.
console.log('bye') // 2.
```

```javascript
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
```

* foo()가 실행되면 출력은 foo - bar - baz - baz end - Helloooo

 ![img](https://miro.medium.com/max/800/1*i9nTlOSPH3q-sCd5-WHg-g.png) 

[자바스크립트 동작 원리]( [https://engineering.huiseoul.com/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%9E%91%EB%8F%99%ED%95%98%EB%8A%94%EA%B0%80-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%A3%A8%ED%94%84%EC%99%80-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%98-%EB%B6%80%EC%83%81-async-await%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%BD%94%EB%94%A9-%ED%8C%81-%EB%8B%A4%EC%84%AF-%EA%B0%80%EC%A7%80-df65ffb4e7e](https://engineering.huiseoul.com/자바스크립트는-어떻게-작동하는가-이벤트-루프와-비동기-프로그래밍의-부상-async-await을-이용한-코딩-팁-다섯-가지-df65ffb4e7e) )

## 8. axios

* axios는 비동기 구조의 한계점을 해결하기 위한 새로운 방법이다.

```javascript
console.log('hi')
axios.get('https://jsonplaceholder.typicode.com/posts/1') // 요청을 보내고
    .then( response => {        // 끝난다면 그때 함수를 실행 해 달라
        console.log(response)
        return response.data
    })
console.log('bye')
```

* axios로 보낸 요청 결과가 온다면 바로 실행될 수 있도록 한다.
* callback function을 일일이 쌓을 필요 없이 사용할 수 있다.

### 1. Django 좋아요 javascript로 비동기형식 만들기

```html
<i id="like-button" data-id="{{article.id}}" class="fas fa-heart fa-2x" style="color: red;"></i>
```

* data-X : X에 관한 값들을 저장한다.

```json
dataset = {
    id: ....,
    name: .....,
    .....
}
```

* django에서 데이터값을 .json형식으로 보낼 수 있다.

```python
# views.py
from django.http import JsonResponse
@login_required
def like(request, article_pk):
    # 좋아요를 눌렀다면
    article = Article.objects.get(pk=article_pk)
    if request.user in article.like_users.all():
        # 좋아요 취소 로직
        article.like_users.remove(request.user)
        is_liked = False
    # 아니면
    else:
        # 좋아요 로직
        article.like_users.add(request.user)
        is_liked = True
    
    context = {
        'is_liked': is_liked, 
        'like_count': article.like_users.count()
        }
    return JsonResponse(context)
```

* 좋아요를 담당하는 html 태그를 가지고 와서 변형한다.

```html
<!-- detail.html -->
<script>
    const likeButton = document.querySelector('#like-button')
    likeButton.addEventListener('click', function (event) {
        console.log(event.target.dataset.id) // 미리 저장한 article.id를 불러온다
        axios.get(`/articles/${event.target.dataset.id}/like/`) // 주소로 요청
            .then(response => {
                console.log(response) // 요청받은 데이터 확인
                console.log(event.target) // 현재 html 파일에 있는 데이터
                const likeCount = document.querySelector('#like-count')
                if (response.data.is_liked){
                    event.target.classList.remove('far')
                    event.target.classList.add('fas')
                    likeCount.innerText = `${response.data.like_count}`
                }
                else
                {
                    event.target.classList.remove('fas')
                    event.target.classList.add('far')
                    likeCount.innerText = `${response.data.like_count}`
                }
            })
    })
</script>
```

### 2. POST 형식으로 변경하기

```javascript
<script>
    const likeButton = document.querySelector('#like-button')
    likeButton.addEventListener('click', function (event) {
        console.log(event.target.dataset.id)
        axios.defaults.xsrfCookieName = 'csrftoken'  // csrf token cookie
        axios.defaults.xsrfHeaderName = 'X-CSRFToken' // csrf token header
        axios.post(`/articles/${event.target.dataset.id}/like/`)  // axios post형식 변경
            .then(response => {
                console.log(response)
                console.log(event.target)
                const likeCount = document.querySelector('#like-count')
                if (response.data.is_liked){
                    event.target.classList.remove('far')
                    event.target.classList.add('fas')
                    likeCount.innerText = `${response.data.like_count}`
                }
                else
                {
                    event.target.classList.remove('fas')
                    event.target.classList.add('far')
                    likeCount.innerText = `${response.data.like_count}`
                }
            })
            .catch(error=>{
                console.log(error)
            })
    })
```

### 3. views.py like함수 분기를 위한 설정

```python
@login_required
def like(request, article_pk):
    # 좋아요를 눌렀다면
    # django는 모든 데이터를 request를 이용해 판단하기 때문에 요청을 보내면서 필요한 header를 보내줘야 한다.
    if request.is_ajax():  # 분기를 위한 설정 => javascript 에 추가 명령어 필요
        article = Article.objects.get(pk=article_pk)
        if request.user in article.like_users.all():
            # 좋아요 취소 로직
            article.like_users.remove(request.user)
            is_liked = False
        # 아니면
        else:
            # 좋아요 로직
            article.like_users.add(request.user)
            is_liked = True
        
        context = {
            'is_liked': is_liked, 
            'like_count': article.like_users.count()
            }
        return JsonResponse(context)
    else:
        return HttpResponseForbidden()
```

```javascript
<script>
    const likeButton = document.querySelector('#like-button')
    likeButton.addEventListener('click', function (event) {
        console.log(event.target.dataset.id)
        // POST 요청 csrftoken을 AJAX 요청시 설정하는 법
        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = 'X-CSRFToken'
        // django is_ajax() 분기가 되는 기준이 아래의 헤더 설정에 따라서 진행
        axios.defaults.headers.common['X-REQUESTED-WITH'] = 'XMLHttpRequest'
        ......
</script>
```



## 9. promise

### 1. 비동기 처리

```javascript
// 데이터를 외부로부터 받아와서 변수에 저장하고 출력하는 함수
// 1. 비동기 X
function getData() {
    const data = {'data': 'some data'}
    return data
}

let response = getData()
console.log(response)

// 2. setTimeout
function getData() {
    let data
    setTimeout(function () {
        console.log('요청을 보냈습니다.')
        data = {'data': 'some data'}
    }, 1000)
    return data
}

let response1 = getData()
console.log(response1)  // undefined
```

### 2. 비동기 처리를 위한 callback 함수 정의

* 해당 작업을 하는 함수를 인자로 받아서 나중에 callback함수를 부른다.

```javascript
// 3. callback function 정의
function getDataCallback(callback) {
    // callback = 저함수
    setTimeout(function(){
        console.log('요청을 보냈습니다.')
        const data = {'data': 'some data'} // 데이터 도착
        callback(data) // 내가 원하는 작업 시작
    }, 1000)
}

// 함수 호출, 인자로 함수를 넘겨주는데 그게 출력하는 작업
getDataCallback(function(data) {
    let response2 = data
    console.log(response2)
})
```

### 3. promise

* Promise object를 리턴한다. 나중에(작업이 끝나면) then/catch를 실행한다.

```
promise object 상태
- pending -> 작업 진행중
- resolved -> resolve 함수 호출(작업 성공시)
- rejected -> reject 함수 호출(작업 실패시)

resolve -> then에서 처리, reject -> catch에서 처리
```

```javascript
function getDataPromise() {
    return new Promise(resolve => {
        setTimeout(function(){
            console.log('요청을 보냈습니다.')
            const data = {'data': 'some data'} // 데이터 도착
            resolve(data) // 내가 원하는 작업 시작
        }, 1000)
    })
}

let response3 = getDataPromise()
console.log(response3)  // 1. 출력(pending)
// 다시 확인하면
console.log(response3) // 2. 출력 (resolved)
response3.then(response => console.log(response)) // 3. data 출력

getDataPromise()
    .then(response => console.log(response3))
```

### 4. async / await

```javascript
function getDataPromise() {
    return new Promise(resolve => {
        setTimeout(function(){
            console.log('요청을 보냈습니다.')
            const data = {'data': 'some data'} // 데이터 도착
            resolve(data) // 내가 원하는 작업 시작
        }, 1000)
    })
}

async function printData() {
    const response = await getDataPromise()
    console.log(response)
}
```
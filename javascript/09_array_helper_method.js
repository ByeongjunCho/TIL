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
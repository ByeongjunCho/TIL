
function sum(x, callbackfn) {
    setTimeout(callbackfn, 100, x+1)
    
}

var result = 0
sum(2, function(x){
    result = x
    console.log(result)  // 3
})
console.log(result)  // 0


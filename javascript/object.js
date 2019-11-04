const me = {
    name: 'tak',
    phone: '010-1234-5678',
    // 메서드에서도 arrow function 사용 금지
    greeting: function() {
        return 'hi, ' + this.name
    }
}

// object 함수 구현
const Person = function(name, phone){
    this.name = name
    this.phone = phone
    this.greeting = function(){
        return 'hi, ' + this.name
    }
}

const lee = new Person('hu', '123-456-7890')

// 생성자 함수에서는 arrow function 사용 금지
const Animal = name => {
    this.name = name
}

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
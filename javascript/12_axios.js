console.log('hi')

axios.get('https://jsonplaceholder.typicode.com/posts/1') // 요청을 보내고
    .then( response => {        // 끝난다면 그때 함수를 실행 해 달라
        console.log(response)
        document.write(`
            <h1>${response.data.title} : ${response.data.title}</h1>
            <p>${response.data.body}</p>
        `)
        return response.data
    })
console.log('bye')
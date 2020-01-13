# React 기초

## 준비사항

> vs extentions 설치

* ESLint
* ES7 React/Redux/GraphQL/React....
* Prettier - Code formatter
* Ranbow Brackets

webpack 설치

```bash
npx create-react-app my-app
cd my-app
npm start
```

## 기본구조

> Component : 데이터를 입력받아 DOM Node를 출력하는 함수

> Conceptually, components are like JavaScript **functions**. They accept arbitrary inputs (called “props”) and return React elements describing what should appear on the screen.

```react
// App.js
import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">

      </div>
    );
  }
}

export default App;
```

- `render` : 컴포넌트가 나에게 보여주는 것

```react
//index.js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
```

> React : UI라이브러리
>
> ReactDom : 웹사이트에 React를 출력
>
> reactNative : 모바일에 React를 올리고 싶은 경우

- ReactDom은 단 한개의 Component를 출력한다.

## React Component

```react
import React, {Component} from 'react';
import './Movie.css';

class Movie extends Component{
  render(){
    return(
      <div>
        <MoviePoster />
        <h1>hello this is a movie</h1>
      </div>
    )
  }
}

class MoviePoster extends Component{
  render(){
    return(
      <img src="https://t1.daumcdn.net/cfile/tistory/24E61F335966F29A15" />
    )
  }
}
export default Movie;
```

> 컴포넌트 -> render -> return -> jsx 순으로 구성됨

## props/stats

```react
// App.js
import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
const movies = [
    'abc',
    'def'
]
class App extends Component {
  render() {
    return (
      <div className="App">
		<Movie title= {movies[0]} />
         <Movie title = {movies[1]} />
      </div>
    );
  }
}

export default App;
```

```react
import React, {Component} from 'react';
import './Movie.css';

class Movie extends Component{
  render(){
    console.log(this.props)
    return(
      <div>
        <MoviePoster />
        <h1>hello this is a movie</h1>
        <h1>{this.props.title}</h1>
      </div>
    )
  }
}
```

> 출력 -> 'abc'     'def'
>
> App.js -> Movie.js로 데이터를 보낼 수 있으며 Movie.js에서는 `props`를 이용하여 데이터를 확인할 수 있음

## props 확인

```react
import React, {Component} from 'react';
import './Movie.css';
import propTypes from 'prop-types'

class Movie extends Component{

  static propTypes = {
    title: propTypes.string.isRequired,
    poster: propTypes.string
  }
  render(){
    console.log(this.props)
    return(
      <div>
        <MoviePoster poster={this.props.poster}/>
        <h1>{this.props.title}</h1>
      </div>
    )
  }
}

class MoviePoster extends Component{
  static propTypes={
    poster: propTypes.string.isRequired
  }
  render(){
    console.log(this.props.poster)
    return(
      <img src={this.props.poster} />
    )
  }
}
export default Movie;
```

> props 변수명 : propTypes.{형식}.{필수여부} 
>
> props입력값의 형식과 필수여부를 결정한다.



## Component 구조

>  // Render : componentWillMount -> render() -> componentDidMount()
>
>  // Update componentWillReceiveProps() -> shouldComponentUpdate() -> componentWillUpdate() -> render() -> componentDidupdate()

## state

- component의 state가 변경되면, render가 다시 실행

```react
  
state = {
    greeting: "Hello!"
  }

  componentDidMount(){
    setTimeout(() => {
      this.setState({
        greeting: 'Hello again!'
      })
    }, 5000)
  }
```

> state를 직접 변경할 수 없음 ex) this.state.greeting = "adffsd" 

```react
componentDidMount(){
    setTimeout(() => {
      this.setState({
        movies: [
          ...this.state.movies,   // <= this.state.movies : 현재값
          {
            title: "Transpotting",
            poster: "https://m.media-amazon.com/images/M/MV5BMTM0NjQ4OTgyNV5BMl5BanBnXkFtZTcwOTU2MzQ4Nw@@._V1_CR0,60,640,360_AL_UX477_CR0,0,477,268_AL_.jpg"
          }
        ]
      })
    }, 1000)
  }
```

> ...this.state.movies 가 존재하지 않으면 `state`의 movies는 새로운 것으로 대체됨
>
> infiniting movings

## jsx 기본구조

```jsx
<div>
    <div>
        Hello
      </div>
      <div>
        Bye
	</div> 
</div>
```

- 혹은 아래와 같이`Fragment`사용(v16.2 이상)

```jsx
<Fragment>
        <div>
          Hello
        </div>
        <div>
          Bye
        </div>
</Fragment>
```

## JSX 내부에서 조건부 렌더링

- JSX에서 조건부 렌더링 사용을 위해서는 삼항 연산자 혹은 AND 연산자 사용
- if문 사용 불가(IIFE : 즉시 실행 함수 표현) 사용 필요

```jsx
import React, { Component, Fragment } from "react";

class App extends Component {
  render() {
    const name = "react";
    return (
      <Fragment>
        <div>Hello {name}</div>
        <div>Bye</div>

        <div>{1 + 1 === 3 ? <div>맞아요!</div> : <div>틀려요!</div>}</div>
        <div>{1+1 === 2 && (<div>맞아요!</div>)}</div>

      </Fragment>
    );
  }
}

export default App;

```

> 조건문 ? true일 경우 : false인 경우
>
> 조건문 && true인 경우

- 조건문이 복잡하면 JSX밖에서 로직을 작성하는 것이 좋음
- 꼭 작성해야 한다면, IIFE를 사용하여 작성

```jsx
import React, { Component, Fragment } from "react";

class App extends Component {
  render() {
    const value = 1;
    return (
      <Fragment>
        <div>
          {(function() {
            if (value === 1) return <div>하나</div>;
            if (value === 2) return <div>둘</div>;
            if (value === 3) return <div>셋</div>;
          })()
          }
        </div>
      </Fragment>
    );
  }
}

export default App;
```

## style과 className

```jsx
import React, { Component } from 'react';

class App extends Component {
  render() {
    const style = {
      backgroundColor: 'black',
      padding: '16px',
      color: 'white',
      fontSize: '12px'
    };

    return (
      <div style={style}>
        hi there
      </div>
    );
  }
}

export default App;
```

- html에서 텍스트형태로 지정하는 style과는 다르게 react에서는 객체 형태로 작성해야 한다.

> react에서 html 태그 class 설정 시 className을 사용해야 함

App.css

```css
.App {
  background: black;
  color: aqua;
  font-size: 36px;
  padding: 1rem;
  font-weight: 600;
}
```

App.js

```jsx
import React, { Component } from 'react';
import './App.css'

class App extends Component {
  render() {
    return (
      <div className="App">
        리액트
      </div>
    );
  }
}
export default App;
```



## 새 컴포넌트 만들기

```jsx
import React, { Component } from 'react';

class MyName extends Component {
  render() {
    return (
      <div>
        안녕하세요! 제 이름은 <b>{this.props.name}</b> 입니다.
      </div>
    );
  }
}
export default MyName;
```

- 컴포넌트가 받은 props 값은 `this.`키워드를 통해 조회가 가능하다

```jsx
import React, { Component } from 'react';
import MyName from './MyName';

class App extends Component {
  render() {
    return (
      <MyName name="리액트" />
    );
  }
}

export default App;
```

## defaultProps

* props의 default값을 설정할 수 있음

```jsx
import React, { Component } from 'react';
// 함수형 컴포넌트 설정
class MyName extends Component {
  static defaultProps = {
    name: '기본이름'
  }
  render() {
    return (
      <div>
        안녕하세요! 제 이름은 <b>{this.props.name}</b> 입니다.
      </div>
    );
  }
}

export default MyName;
```

* 다음과 같이 설정도 가능하다

```jsx
import React, { Component } from 'react';

class MyName extends Component {
  render() {
    return (
      <div>
        안녕하세요! 제 이름은 <b>{this.props.name}</b> 입니다.
      </div>
    );
  }
}

MyName.defaultProps = {
  name: '기본이름'
};

export default MyName;
```

**이렇게 defaultProps를 설정하면**

```jsx
import React, { Component } from 'react';
import MyName from './MyName';

class App extends Component {
  render() {
    return (
      <MyName />
    );
  }
}
export default App;
```

**defaultProps**가 출력되는 것을 확인할 수 있다.
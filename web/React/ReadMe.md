# React 기초

## React Component

```jsx
// App.js
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
```

- `render`함수 필수
- `export default`가 있어야 해당 컴포넌트를 다른 곳에서 사용할 수 있음

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
```

- import {component} form './{path}'로 컴포넌트를 불러옴
- 브라우저에서 리액트 컴포넌트를 보여주기 위해 `ReactDOM.render`함수 사용

>ReactDOM.render(렌더링 할 결과물, 컴포넌트를 그릴 DOM)

## jsx 기본구조

```jsx
import React, { Component } from 'react';

class App extends Component {
  render() {
    return (
      <div>
        
      </div>
    );
  }
}

export default App;
```

- 언제나 태그는 닫혀있어야 함
- 두 개 이상의 엘리먼트는 하나의 엘리먼트로 감싸져있어야 함

```jsx
// src/App.js
import React, { Component } from 'react';

class App extends Component {
  render() {
    return (
      <div>
        Hello
      </div>
      <div>
        Bye
      </div> // => 에러 발생(2개의 엘리먼트)
    );
  }
}

export default App;
```

- 위의 코드를 수정하여 하나의 엘리먼트로 감싸도록 수정해야 함

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

## JSX 안에 자바스크립트 값 사용하기

- JSX 내부에서 자바스크립트 변수값을 사용하기 위해서는 `{}`를 사용

```jsx
import React, { Component } from 'react';

class App extends Component {
  render() {
    const name = 'react';
    return (
      <div>
        hello {name}!
      </div>
    );
  }
}

export default App;
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
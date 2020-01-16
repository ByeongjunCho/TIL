import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import Movie from './Movie.js'


class App extends Component {
  // Render : componentWillMount -> render() -> componentDidMount()
  // Update componentWillReceiveProps() -> shouldComponentUpdate() -> componentWillUpdate() -> render() -> componentDidupdate()
  componentWillMount(){ 
    console.log('will mount')
  }

  state = {
    greeting: "Hello!",
  }

  componentDidMount(){
    fetch('https://yts.lt/api/v2/list_movies.json?sort_by=rating')
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(err=> console.log(err))
  }

  _renderMovies = () => {
    const movies = this.state.movies.map((movie, index) => {
      return <Movie title={movie.title} poster={movie.poster} key={index} />
    })

    return movies
  }
  
  render() {
    console.log('did render')
    return (
      <div className="App">
        {this.state.movies ? this._renderMovies() : 'Loading'}
      </div>
    );
  }
}

export default App;

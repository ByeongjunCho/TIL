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
    setTimeout(() => {
      this.setState({
        movies : [
          {
            title: "Matrix",
            poster: "https://633987.smushcdn.com/907311/wp-content/uploads/2019/08/lede-the-matrix-1300x731.jpg?lossy=1&strip=1&webp=1"
          },
          {
            title: "StarWars",
            poster: "https://lumiere-a.akamaihd.net/v1/images/tros-hero-in-theaters-mobile-a_e8a421c0.jpeg?region=0,0,1024,626&width=960"
          },
          {
            title: "Oldboy",
            poster: "https://miro.medium.com/max/3910/1*PEYbHg2nNJ1Rxa_3slLweg.jpeg",
        
          },
          {
            title: "Hungergame",
            poster: "https://m.media-amazon.com/images/M/MV5BMTM0NjQ4OTgyNV5BMl5BanBnXkFtZTcwOTU2MzQ4Nw@@._V1_CR0,60,640,360_AL_UX477_CR0,0,477,268_AL_.jpg"
          }
        
        ]
      })
    }, 5000)
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

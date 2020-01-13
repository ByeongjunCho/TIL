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
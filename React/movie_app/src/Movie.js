import React, {Component} from 'react';
import './Movie.css';
import propTypes from 'prop-types'

// class Movie extends Component{

//   static propTypes = {
//     title: propTypes.string.isRequired,
//     poster: propTypes.string
//   }
//   render(){
//     console.log(this.props)
//     return(
//       <div>
//         <MoviePoster poster={this.props.poster}/>
//         <h1>{this.props.title}</h1>
//       </div>
//     )
//   }
// }

// class MoviePoster extends Component{
//   static propTypes={
//     poster: propTypes.string.isRequired
//   }
//   render(){
//     console.log(this.props.poster)
//     return(
//       <img src={this.props.poster} alt="Movie Poster"/>
//     )
//   }
// }

// props만 필요한 필요한(리턴하는) 경우 fuctional component를 만들어서 사용
function MoviePoster({poster}){
  return (
    <img src={poster} alt="Movie Poster"/>
  )
}


function Movie({title, poster}){
  return(
    <div>
        <MoviePoster poster={poster}/>
        <h1>{title}</h1>
      </div>
  )
}

MoviePoster.propTypes={

}
MoviePoster.propTypes={
  poster: propTypes.string.isRequired
}
export default Movie;
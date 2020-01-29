import React, {Component} from 'react';

class App extends Component{
  state={
    image: null
  };

  handleChange = (event) => {
    this.setState({
      file: URL.createObjectURL(event.target.files[0])
    })
  }

  render(){
  return (
    <div>
        <input type="file" onChange={this.handleChange}/>
        <img src={this.state.file}/>
        <p>{this.state.file}</p>
    </div>
  );
  }
}

export default App;

import React, { Component } from 'react';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = { verse: 'Loading...' };
  }

  componentDidMount() {
    fetch('/api/verse/Genesis/1/1')
      .then(r => r.json())
      .then(data => this.setState({ text: data.text }));
  }

  render() {
    return (
      <div>
        <h1>fastapi-react-demo</h1>
        <p>Result of API call: {this.state.text}</p>
      </div>
    );
  }
}

export default App;

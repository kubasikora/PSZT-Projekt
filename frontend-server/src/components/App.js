import React, { Component } from 'react';
import EntryPage from './EntryPage';

import './App.css';

class App extends Component {
  onClickHandler(){
    console.log('handling the click...')

  }

  render() {
    return (
      <EntryPage />
    );
  }
}

export default App;


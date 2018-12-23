import React, { Component } from 'react';
import AlgorithmPage from './AlgorithmPage';
import EntryPage from './EntryPage';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

class App extends Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route path="/" exact component={EntryPage}/>
          <Route path="/home" exact component={AlgorithmPage} />
        </Switch>       
      </Router>
    );
  }
}

export default App;


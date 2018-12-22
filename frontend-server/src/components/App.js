import React, { Component } from 'react';
import AlgorithmPage from './AlgorithmPage';
import EntryPage from './EntryPage';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import PageTransition from "react-router-page-transition";

import './App.css';

class App extends Component {
  render() {
    return (
      <Router>
       {/*} <Route
          render={({location}) => ( */}
            <PageTransition timeout={500}>
              <Switch>
                <Route path="/" exact component={EntryPage}/>
                <Route path="/home" exact component={AlgorithmPage} />
              </Switch>   
            </PageTransition> 
          {/*})} />*/}    
      </Router>
    );
  }
}

export default App;


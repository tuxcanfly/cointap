import React, { Component } from 'react'
import { HashRouter as Router, Route } from 'react-router-dom'; 
import { Switch, Link, IndexRoute, browserHistory } from 'react-router'

import { PageForm } from './page'

class App extends Component {
  render() {
    return (
      <Router>
          <Switch>
              <Route name="index" path='/' render={() => (<PageForm url="api/send/" />)} />
          </Switch>
      </Router>
    )
  }
}

export default App

import React, { Component } from "react";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";
// import ArtistList from "./components/ArtistList";
// import Artist from "./components/Artist";
import "./App.css";

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <div className="App">Hello World</div>
          <Switch>
            {/* <Route exact path='/posts/:id' component={Post}></Route>
      <Route path='/' component={Posts}></Route> */}
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;

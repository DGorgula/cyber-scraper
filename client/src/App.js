import { useEffect, useRef, useState } from 'react';
import axios from 'axios'
import { BrowserRouter, Switch, Route, Redirect } from 'react-router-dom'
import './App.css';
import Post from './components/Post/Post';
import Lobby from './components/Lobby/Lobby';
function App() {
  const [chosenPost, setChosenPost] = useState()

  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route exact path="/">
            <Lobby setChosenPost={setChosenPost} chosenPost={chosenPost} />
          </Route>
          <Route path="/post/:postTitle">
            <Post setChosenPost={setChosenPost} chosenPost={chosenPost} />
          </Route>
          <Route path="*">
            <Redirect to="/" />
          </Route>
        </Switch>

      </BrowserRouter>

    </div>
  );
}

export default App;

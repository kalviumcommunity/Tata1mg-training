import './App.css';
import {BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from './components/Home/Home';
import Sidebar from './components/Sidebar/Sidebar';

function App() {
  return (
    <div className="App">
      <Sidebar />
      <div className='other'>
      <Routes>
      <Route index element = {<Home />}></Route>
      </Routes>
      </div>
      
    </div>
  );
}

export default App;

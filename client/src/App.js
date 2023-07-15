import "./App.css";
import { Routes, Route } from "react-router-dom";
import Home from "./components/Home/Home";
import Sidebar from "./components/Sidebar/Sidebar";
import Login from "./components/Login/Login";
import SignUp from "./components/Signup/Signup";
import PostDetail from "./components/PostDetail/PostDetail";

function App() {
  return (
    <div className="App">
      <Sidebar />
      <div className="other">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/login" element={<Login />} />
          <Route path="/detail" element={<PostDetail />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;

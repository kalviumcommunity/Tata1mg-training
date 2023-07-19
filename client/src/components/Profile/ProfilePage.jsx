import React from "react";
// import Signup from "../Signup/Signup";
import "./ProfilePage.css";
const ProfilePage = () => {
  return (
    <div>
      <div className="upper-portion">
        <img src="cover image" alt="cover-image" className="cover-image" />
        <div className="mid-portion">
          <img src="" alt="user-pic" className="user-pic" />
          <h1 className="username">{/* {us er.userName} */}</h1>
        </div>
      </div>
      <div className="details">
        <button className="post-button">Posted</button>
        <button className="create-button">Created</button>
      </div>
      <div>{/* Extra space */}</div>
    </div>
  );
};

export default ProfilePage;

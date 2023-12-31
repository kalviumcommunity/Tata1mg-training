import React, {useState, useEffect} from 'react'
import axios from 'axios';
import "./Details.css"
import {AiOutlineArrowRight} from "react-icons/ai"
import Masonry from 'react-masonry-css';

const PostDetail = () => {
  const [image, setImage] = useState('')
  const [userpic, setUserpic] = useState('')
  const [userpic1, setUserpic1] = useState('')
  const [similarList, setSimList] = useState([])

  useEffect(() => {
    const fetchImage = async () => {
      try {
        const url = `https://api.unsplash.com/photos/random?client_id=${process.env.REACT_APP_API_KEY}&count=20`;
        const response = await axios.get(url);
        const images = response.data;
        setImage(images[0].urls.regular);
        setUserpic(images[1].urls.regular)
        setUserpic1(images[2].urls.regular)
      } catch (error) {
        console.error('Failed to retrieve image:', error);
      }
    };

    fetchImage();
  }, []);

  useEffect(() => {
    const fetchSimImages = async () => {
      try {
        const url = `https://api.unsplash.com/photos/random?client_id=${process.env.REACT_APP_API_KEY}&count=560`;
        const response = await axios.get(url);
        const images = response.data;
        setSimList(images);
      } catch (error) {
        console.error('Failed to retrieve images:', error);
      }
    };

    fetchSimImages();
  }, []);

  const breakpointColumnsObj = {
    default: 3,
    1100: 2,
    700: 1,
  };

  return (
    <div className='main'>
      <div className="mainthing">
        <div className="imagecont">
        <img src={image} alt="randomimage" className='post'/>
        </div>
        <div className="details">
          <div className="detail">
            <h1 id='posttitle'>Title</h1>
            <div className="userdet">
              <img src={userpic} alt="userpic" className='userpic'/>
              <h3 id='usern'>Name</h3>
            </div>
          </div>
          <div className="comments">
            <h1 id='postcom'>Comments</h1>
            <div className="commenter">
            <img src={userpic1} alt="userpic" className='userpic'/>
              <input type="text"className='commentbox'/>
              <button id='ptcom'><AiOutlineArrowRight style={{backgroundColor: '471192'}}/></button>
            </div>
          </div>
        </div>
      </div>
      <div className="sim">
        <h1 id='simposts'> Similar Posts</h1>
        <Masonry
        breakpointCols={breakpointColumnsObj}
        className="masonry"
        columnClassName="masonrycolumn"
      >
        {similarList.map((image) => (
           <div key={image.id} className="images">
          <img
            key={image.id}
            src={image.urls.regular}
            alt={image.alt_description}
            className="img"
          />
          </div>
        ))}
      </Masonry>
      </div>
    </div>
  )
}

export default PostDetail

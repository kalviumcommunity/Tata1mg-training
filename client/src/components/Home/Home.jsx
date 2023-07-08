import React, { useEffect, useState } from 'react';
import "./Home.css";
import axios from 'axios';
import Masonry from 'react-masonry-css';

const Home = () => {
  const [imageList, setImageList] = useState([]);

  console.log(`${process.env.REACT_APP_API_KEY}`);

  useEffect(() => {
    const fetchImages = async () => {
      try {
        const url = `https://api.unsplash.com/photos/random?client_id=${process.env.REACT_APP_API_KEY}&count=560`;
        const response = await axios.get(url);
        const images = response.data;
        setImageList(images);
      } catch (error) {
        console.error('Failed to retrieve images:', error);
      }
    };

    fetchImages();
  }, []);

  const breakpointColumnsObj = {
    default: 3,
    1100: 2,
    700: 1,
  };

  return (
    <div>
       <Masonry
        breakpointCols={breakpointColumnsObj}
        className="my-masonry-grid"
        columnClassName="my-masonry-grid_column"
      >
        {imageList.map((image) => (
           <div key={image.id} className="image-item">
          <img
            key={image.id}
            src={image.urls.regular}
            alt={image.alt_description}
            className="image"
          />
          </div>
        ))}
      </Masonry>
    </div>
  );
};

export default Home;

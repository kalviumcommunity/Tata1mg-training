import React, { useState } from 'react'
import "./Sidebar.css"
import { motion } from "framer-motion"
import {AiFillHome} from "react-icons/ai"
import {BiSearch} from "react-icons/bi"
import {FaBars} from "react-icons/fa"

const Sidebar = () => {
  const [open, setOpen] = useState(false);
  const toggle = () => setOpen(!open)

  return (
    <div className='complete-container'>
      <motion.div className='sidebar' animate={{width: open ? "20vw" : "3vw"}}>
        <div className='top'>
          {open && <h1 className='logo'>SocialCircle</h1>}
          <FaBars onClick={toggle} size={35}/>
        </div>
        <div className='sandh'>
          <div className="home">
          <AiFillHome size={35}/>
          {open && <h3>Home</h3>}
          </div>
          <div className="search">
            <BiSearch size={35}/>
            {open && <h3>Search</h3>}
          </div>
        </div>
      </motion.div>
    </div>
  )
}

export default Sidebar

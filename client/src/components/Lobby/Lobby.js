import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { baseUrl } from '../../env.json'
import PostImage from '../PostImage/PostImage';
import './Lobby.css'

function Lobby({ setChosenPost }) {
    const [allPosts, setAllPosts] = useState([])
    useEffect(() => {
        console.log(baseUrl);
        axios.get(`${baseUrl}/post/all`)
            .then(res => {
                console.log(res.data["allPosts"]);
                setAllPosts(res.data["allPosts"]);
            })
            .catch(console.log)

    }, [])
    return (
        <div id="lobby">

            <h1 className="title">CyberNews Scraper</h1>
            {allPosts.map((post, i) => {
                return <PostImage key={i} setChosenPost={setChosenPost} postData={post} />
            })}
        </div>
    )
}

export default Lobby

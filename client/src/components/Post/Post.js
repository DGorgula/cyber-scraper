import React from 'react'
import { useHistory } from 'react-router';
import './Post.css';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';

function Post({ postData, setChosenPost, chosenPost }) {
    console.log(chosenPost);
    const history = useHistory();
    if (!chosenPost) history.push("/");
    return (
        <div id="post">
            <ArrowBackIcon id="back-button" onClick={() => { setChosenPost(false); history.push("/") }} />
            <h1 className="title">{chosenPost.title}</h1>
            <div id="post-title">
                <img src={chosenPost.image} alt={chosenPost.title} />
                <div id="post-data">
                    <div className="publish-date">
                        <AccessTimeIcon className="time-icon" />
                        <time>{chosenPost["publish-date"]}</time>
                    </div>
                    <p id="author">{chosenPost.Author}</p>
                </div>
            </div>
            <div className="content">

                {chosenPost.content.split("\\n\\n\\n").map((paragraph, i) => {
                    return <p key={i}>{paragraph.replaceAll("\\n", "\n")}</p>
                })}
            </div>
        </div>
    )
}

export default Post
import React from 'react'

function Post({ postData, setChosenPost, chosenPost }) {
    console.log(chosenPost);
    return (
        <div id="post">
            <h1>{chosenPost.title}</h1>
            <time>{chosenPost["publish-date"]}</time>
            <img src={chosenPost.image} alt={chosenPost.title} />
            <p id="author">{chosenPost.Author}</p>
            <div className="content">

                {chosenPost.content.split("\\n").map(paragraph => {
                    return <p>{paragraph}</p>
                })}
            </div>
        </div>
    )
}

export default Post

import React from 'react'
import Tooltip from '@mui/material/Tooltip';
import { useHistory } from 'react-router';

function PostImage({ postData, setChosenPost }) {
    const history = useHistory();
    return (
        <div>
            <Tooltip title={postData.title} followCursor={true}>
                <img className="post-image" src={postData.image} alt={postData.title} onClick={() => {
                    setChosenPost(postData)
                    history.push(`/post/${postData.title.replaceAll(" ", "-")}`)
                }} />
            </Tooltip>
        </div>
    )
}

export default PostImage

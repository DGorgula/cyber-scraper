import React from 'react'
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import { useHistory } from 'react-router';

function Author({ authorData, setChosenAuthor, chosenPost }) {
    const { name, image, about } = authorData;
    const history = useHistory();
    return (
        <div>
            <ArrowBackIcon id="back-button" onClick={() => { setChosenAuthor(false); history.push(`/post/${chosenPost.title}`) }} />

            <h1 className="title">{name}</h1>
            <img className="author-image" src={image} alt={name} />
            <p className="about">{about}</p>

        </div>
    )
}

export default Author

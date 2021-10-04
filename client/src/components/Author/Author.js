import React from 'react'

function Author({ authorData }) {
    const { name, image, about } = authorData
    return (
        <div>
            <h1 className="title">{name}</h1>
            <img className="author-image" src={image} alt={name} />
            <p className="about">{about}</p>

        </div>
    )
}

export default Author

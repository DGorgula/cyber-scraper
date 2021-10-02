from flask import Flask, escape, request

#   Dotenv
from dotenv import dotenv_values
import requests
config = dotenv_values(".env")
locals().update(config)

#   RDF
from franz.openrdf.connect import ag_connect
from franz.openrdf.vocabulary import RDF
# from franz.openrdf.vocabulary.xmlschema import XMLSchema

conn = ag_connect('test', host=HOST, port=PORT, user=USER, password=PASS, create=True, clear=True)
basePath = "ex://"
conn.setNamespace('ex', basePath)
post = conn.createURI("http://example.org/ontology/Post")
title = conn.createURI("http://example.org/ontology/title")
name = conn.createURI("http://example.org/ontology/name")
content = conn.createURI("http://example.org/ontology/content")
publishDate = conn.createURI("http://example.org/ontology/publish-date")
link = conn.createURI("http://example.org/ontology/postlink")
image = conn.createURI("http://example.org/ontology/image")
author = conn.createURI("http://example.org/ontology/Author")
about = conn.createURI("http://example.org/ontology/about")


app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name = "Danks-param"):
    queryName = request.args.get("name")
    paramName= name
    return f'Hello, {escape(queryName)}, {escape(paramName)}!'

@app.route('/author/new', methods=['post'])
def postAuthor():
    json = request.get_json()
    print(json)
    authorName = request.get_json()["name"]
    authorAbout = request.get_json()["about"]
    authorImage = request.get_json()["image"]
    newAuthor = conn.createURI(f'http://example.org/author/{authorName.replace(" ", "-")}')
    print(authorName, authorAbout, authorImage)
    conn.add(newAuthor, RDF.TYPE, author)
    conn.add(newAuthor, name, authorName)
    conn.add(newAuthor, about, authorAbout)
    conn.add(newAuthor, image, authorImage)
    return "done"

@app.route('/author/all')
def getAllAuthors():
    authorsData = []
    authors = conn.getStatements(None, None, author).string_tuples
    for a in authors:
        print("a", a[0])
        nextIndex = len(authorsData)
        authorRawData = conn.getStatements(a[0], None, None).string_tuples
        authorsData.append({})
        for data in authorRawData:
            print("data", data)
            p = data[1].replace(">","").split("/")
            if len(p) > 5 : continue
            authorsData[nextIndex][p[4]] = data[2].replace("\'","").replace('\"',"")
    print(dir(authors))
    print(str(authorsData))
    return {"allAuthors": authorsData}

@app.route('/post/new', methods=['post'])
def postPost():
    json = request.get_json()
    postTitle = json["title"]
    postLink = json["link"]
    postImage = json["image"]
    postContent = json["content"]
    postPublishDate = json["publishDate"]
    postAuthor = conn.createURI(f'http://example.org/author/{request.get_json()["author"].replace(" ", "-")}')
    newPost = conn.createURI(f'http://example.org/post/{postTitle.replace(" ", "-")}')
    conn.add(newPost, RDF.TYPE, post)
    conn.add(newPost, title, postTitle)
    conn.add(newPost, link, postLink)
    conn.add(newPost, image, postImage)
    conn.add(newPost, content, postContent)
    conn.add(newPost, publishDate, postPublishDate)
    conn.add(newPost, author, postAuthor)
    return "done"

@app.route('/post/all')
def getAllPosts():
    postsData = []
    posts = conn.getStatements(None, None, post).string_tuples
    for a in posts:
        print("a", a[0])
        nextIndex = len(postsData)
        authorRawData = conn.getStatements(a[0], None, None).string_tuples
        postsData.append({})
        for data in authorRawData:
            print("data", data)
            p = data[1].replace(">","").split("/")
            if len(p) > 5 : continue
            postsData[nextIndex][p[4]] = data[2].replace("\'","").replace('\"',"")
    print(dir(posts))
    print(str(postsData))
    return {"allposts": postsData}

if __name__ == '__main__':
    app.run(debug=True)
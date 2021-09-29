from flask import Flask, escape, request

#   Dotenv
from dotenv import dotenv_values
config = dotenv_values(".env")
locals().update(config)

#   RDF
from franz.openrdf.connect import ag_connect
from franz.openrdf.vocabulary import RDF
# from franz.openrdf.vocabulary.xmlschema import XMLSchema

conn = ag_connect('test', host=HOST, port=PORT, user=USER, password=PASS, create=True, clear=True)
basePath = "ex://"
conn.setNamespace('ex', basePath)
Post = conn.createURI("http://example.org/ontology/Post")
title = conn.createURI("http://example.org/ontology/title")
name = conn.createURI("http://example.org/ontology/name")
content = conn.createURI("http://example.org/ontology/content")
publishDate = conn.createURI("http://example.org/ontology/publish-date")
postLink = conn.createURI("http://example.org/ontology/postlink")
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

@app.route('/author', methods=['post'])
def postAuthor():

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
    return str(authorsData)


if __name__ == '__main__':
    app.run(debug=True)
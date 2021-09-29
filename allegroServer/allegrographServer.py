#   Dotenv
from dotenv import dotenv_values
config = dotenv_values(".env")
locals().update(config)

#   RDF
from franz.openrdf.connect import ag_connect
from franz.openrdf.vocabulary import RDF
from franz.openrdf.vocabulary.xmlschema import XMLSchema
from franz.openrdf.query.query import QueryLanguage

#   datetime
from datetime import date, time, datetime
import iso8601

def createBobAndAlice(conn):
    person = conn.createURI("http://example.org/ontology/Person")
    name = conn.createURI("http://example.org/ontology/name")
    bob = conn.createURI("http://example.org/people/bob")
    bobsName = conn.createLiteral("Bob")
    alice = conn.createURI("http://example.org/people/alice")
    alicesName = conn.createLiteral("Lisa")
    conn.add(bob, RDF.TYPE, person)
    conn.add(bob, name, bobsName)
    conn.add(alice, RDF.TYPE, person)
    conn.add(alice, name, alicesName)


with ag_connect('python-tutorial', host=HOST, port=PORT, user=USER, password=PASS, create=True, clear=True) as conn:
    basePath = "ex://"
    conn.setNamespace('ex', basePath)
    Post = conn.createURI("http://example.org/ontology/Post")
    title = conn.createURI("http://example.org/ontology/title")
    name = conn.createURI("http://example.org/ontology/name")
    content = conn.createURI("http://example.org/ontology/content")
    publishDate = conn.createURI("http://example.org/ontology/publish-date")
    postLink = conn.createURI("http://example.org/ontology/postlink")
    postImage = conn.createURI("http://example.org/ontology/post-image")
    author = conn.createURI("http://example.org/ontology/author")
    d = conn.createLiteral(date(1944, 8, 1))
    t = conn.createLiteral(time(15, 0, 0))
    dt = conn.createLiteral('1944-08-01T17:00:00+02:00', datatype=XMLSchema.DATETIME)
    surprise = conn.createLiteral(iso8601.parse_date('1944-08-01T17:00:00+02:00'))
    
    conn.addTriple('<ex://d>', '<ex://p>', d)
    conn.addTriple('<ex://t>', '<ex://p>', t)
    conn.addTriple('<ex://dt>', '<ex://p>', dt)

    zulu = conn.createLiteral("1944-08-01T15:00:00Z",
                          datatype=XMLSchema.DATETIME)
    print('getStatements():')
    conn.getStatements(None, None, zulu, output=True)
    print()

    print('SPARQL direct match')
    conn.executeTupleQuery('''
        SELECT ?s WHERE {
        ?s ?p "1944-08-01T15:00:00Z"^^xsd:dateTime .
        }''',
        output=True)
    print()

    print('SPARQL filter match')
    conn.executeTupleQuery('''
        SELECT ?s ?o WHERE {
        ?s ?p ?o .
        filter (?o = "1944-08-01T15:00:00Z"^^xsd:dateTime)
        }''',
        output=True)
    print()
    
    # Should be the same...
    print(dt)
    print(surprise)
    print("name", __name__)
    # with statements:
    #     # statements.enableDuplicateFilter()
    #     for statement in statements:
    #         print(*statement)
    # # option 1
    # query = "SELECT ?s ?p ?o WHERE {?s ?p ?o .} ORDER BY ?s ?p ?o"
    # tuple_query = conn.prepareTupleQuery(QueryLanguage.SPARQL, query)
    # result = tuple_query.evaluate()
    # for bindin_set in result:
    #     s = bindin_set.getValue('s')
    #     p = bindin_set.getValue('p')
    #     o = bindin_set.getValue('o')
    #     print(s, p, o)
    # result.close()
    # # option 2
    # allStatements = conn.getStatements()
    # for statement in allStatements:
    #     print(*statement)
    # allStatements.close()


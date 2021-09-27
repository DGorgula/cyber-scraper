#   Dotenv
from dotenv import dotenv_values
config = dotenv_values(".env")
locals().update(config)

#   RDF
from franz.openrdf.connect import ag_connect
from franz.openrdf.vocabulary import RDF

with ag_connect('test', host=HOST, port=PORT, user=USER, password=PASS, clear=True) as conn:
    # print (conn.size())
    person = conn.createURI("http://example.org/ontology/Person")
    name = conn.createURI("http://example.org/ontology/name")
    bob = conn.createURI("http://example.org/people/bob")
    bobsName = conn.createLiteral("Bob")
    alice = conn.createURI("http://example.org/people/alice")
    alicesName = conn.createLiteral("Alice")
    conn.add(bob, RDF.TYPE, person)
    conn.add(bob, name, bobsName)
    conn.add(alice, RDF.TYPE, person)
    conn.add(alice, name, alicesName)

    print (conn.size())
    for statement in conn.getStatements():
        print(statement)
    # conn.add(alice, RDFFormat, person)
    # conn.add(alice, name, alicesName)
    # conn.add(bob, RDFFormat, person)
    # conn.add(bob, name, bobsName)
    # print (conn.size())
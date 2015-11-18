
import os
os.environ['NEO4J_REST_URL'] = 'http://neo4j:admin@localhost:7474/db/data/'

from data_2015_fall.models import *


def mockData():
    users = Author.create(
    {'name':'wei'},
    {'name':'jerry'},
    {'name':'zack'},
    )

    pubs = Article.create(
    {'title':'pub1', 'journal':'IEEE XXX', 'year' : 2015},
    {'title':'pub2', 'journal':'IEEE XXX', 'year' : 2015},
    )
    for user in users:
        user.save()
    for pub in pubs:
        pub.save()


    users[0].articles.connect(pubs[0])
    users[1].articles.connect(pubs[0])
    users[1].articles.connect(pubs[1])
    users[2].articles.connect(pubs[1])

# one example of how to find coauthors
def findCoAuthors():
    wei = Author.nodes.get(name="wei")
    coauthors = set()
    for article in wei.articles.all():
        for coauthor in article.authors.all():
            coauthors.add(coauthor.name)

    print coauthors

findCoAuthors()

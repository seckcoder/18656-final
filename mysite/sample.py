
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
def findCoAuthors(name):
    author = Author.nodes.get(name=name)
    coauthors = set()
    for article in author.articles.all():
        for coauthor in article.authors.all():
            coauthors.add(coauthor)
    return coauthors

def dfs(level, depth, u, coauthors):
    coauthors.add(u)
    if level >= depth: return

    for v in findCoAuthors(u.name):
        if not v in coauthors:
            dfs(level+1, depth, v, coauthors)

def findCoAuthorsMultiLevel(depth, name):
    author = Author.nodes.get(name=name)
    coauthors = set()
    dfs(0, depth, author, coauthors)
    return coauthors

print findCoAuthors("wei")
print findCoAuthorsMultiLevel(2, "wei")

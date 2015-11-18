from neomodel import (StructuredNode, StringProperty, IntegerProperty, ArrayProperty,
    RelationshipTo, RelationshipFrom)

# Create your models here.

class Article(StructuredNode):
    title = StringProperty()
    journal = StringProperty()
    year = IntegerProperty()
    authors = RelationshipFrom('Author', 'AUTHORED')

class Author(StructuredNode):
    name = StringProperty()
    articles = RelationshipTo('Article', 'AUTHORED')
    

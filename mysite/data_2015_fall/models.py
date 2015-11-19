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
    def __str__(self):
        return "<Author: " + self.name + ">"
    def __repr__(self):
        return "<Author: " + self.name + ">"

    def __hash__(self):
        """
        We use name of the author as the hash value
        """
        return hash(self.name)
    def __cmp__(self, other):
        return cmp(self.name, other.name)
        

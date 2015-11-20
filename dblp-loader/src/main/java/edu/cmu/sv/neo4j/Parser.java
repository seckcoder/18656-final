package edu.cmu.sv.neo4j;

import java.io.FileInputStream;
import java.util.*;

import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

public class Parser {
    private Map<String, Long> allAuthors = new HashMap<String, Long>();
    private Map<String, Long> allPublications = new HashMap<String, Long>();
    private Paper paper;
    private String content = null;
    private boolean isNewRecord = false;
    int numRecords = 0;
    
    public void parse() throws Exception {
        SAXParserFactory saxParserFac = SAXParserFactory.newInstance();
        SAXParser parser = saxParserFac.newSAXParser();
        SAXHandler handler = new SAXHandler();
        parser.parse(new FileInputStream("dblp.xml"), handler);
        System.out.println("Complete parsing.");
    }
    
    class SAXHandler extends DefaultHandler {
		@Override
		public void startElement(String uri, String localName, String qName, Attributes attributes) {
			if (numRecords <= 9999) {
				switch (qName) {
				case "paper":
				case "inproceedings":
					paper = new Paper();
					isNewRecord = true;
					paper.key = attributes.getValue("key");
				}
			}
		}

		@Override
		public void endElement(String uri, String localName, String qName) throws SAXException {
			if (isNewRecord) {
				switch (qName) {
				case "author":
					paper.authors.add(content);
					break;
				case "title":
					paper.title = content;
					break;
				case "booktitle":
					paper.booktitle = content;
					break;
				case "year":
					paper.year = Integer.parseInt(content);
					break;
				case "article":
				case "inproceedings":
					numRecords++;
					isNewRecord = false;
					long titleNodeId;
					if (allPublications.containsKey(paper.title)) {
						titleNodeId = allPublications.get(paper.title);
					} else {
						titleNodeId = GraphDb.createPublication(paper.title);
						allPublications.put(paper.title, titleNodeId);
					}

					for (String author : paper.authors) {
						long authorNodeId;
						if (allAuthors.containsKey(author)) {
							authorNodeId = allAuthors.get(author);
						} else {
							authorNodeId = GraphDb.createAuthor(author);
							allAuthors.put(author, authorNodeId);
						}
						GraphDb.createRelationship(titleNodeId, authorNodeId);
					}
					System.out.println(numRecords + ": " + paper);
				}
			}
		}

		@Override
		public void characters(char ch[], int start, int length) {
			if (isNewRecord) {
				content = new String(ch, start, length).trim();
			}
		}
    }
    public static void main(String args[]) throws Exception{
        System.out.println("Reading XML file.");
        System.setProperty("entityExpansionLimit", "1000000");
        GraphDb.open();
        Parser parser = new Parser();
        parser.parse();
        GraphDb.close();
    }
}

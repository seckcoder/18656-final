package edu.cmu.sv.neo4j;

import java.io.File;
import java.util.*;

import org.neo4j.graphdb.*;
import org.neo4j.unsafe.batchinsert.BatchInserter;
import org.neo4j.unsafe.batchinsert.BatchInserters;

public class GraphDb {
	public static final String DB_PATH = "target/neo4j-dblp";
	public static final String NODE_TYPE = "node_type";
	public static final String AUTHOR_NAME_KEY = "name";
	public static final String PUBLICATION_TITLE_KEY = "title";
    public static final String JOURNAL = "journal";
    public static final String YEAR = "year";
    public static final String VOLUME = "volume";

	public static BatchInserter batchInserter;
	public static GraphDatabaseService graphDb;

	public static long createAuthor(String name) {
		Map<String, Object> properties = new HashMap<String, Object>();
		properties.put(AUTHOR_NAME_KEY, name);
		properties.put(JOURNAL, "");
		properties.put(YEAR, 2015);
		properties.put(VOLUME, 1000);
		Label label = DynamicLabel.label("Author");
		long id = batchInserter.createNode(properties, label);
		return id;
	}

	public static long createPublication(String title) {
		Map<String, Object> properties = new HashMap<String, Object>();
		properties.put(PUBLICATION_TITLE_KEY, title);
		Label label = DynamicLabel.label("Article");
		long id = batchInserter.createNode(properties, label);
		return id;
	}

	public static void createRelationship(long publicationNodeId, long authorNodeId) {
		RelationshipType hasAuthor = DynamicRelationshipType.withName("AUTHORED");
		batchInserter.createRelationship(publicationNodeId, authorNodeId, hasAuthor, null);
		batchInserter.createRelationship(authorNodeId, publicationNodeId, hasAuthor, null);
	}

	@SuppressWarnings("deprecation")
	public static void open() {
		batchInserter = BatchInserters.inserter(new File(DB_PATH).getAbsolutePath());
	}

	public static void close() {
		batchInserter.shutdown();
	}
}

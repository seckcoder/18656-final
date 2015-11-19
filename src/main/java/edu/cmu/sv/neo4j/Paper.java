package edu.cmu.sv.neo4j;
import java.util.ArrayList;


public class Paper {
    public String key;
    public String title;
    public String booktitle;
    int year;
    public ArrayList<String> authors;
    
    public Paper(){
        key = "";
        title = "";
        booktitle = "";
        year = 0;
        authors = new ArrayList<String>();
    }
    @Override
    public String toString(){
        return key+" "+title+" "+booktitle+" "+year+" "+authors.toString();
    }
}

# 18656-final
18656-final


slack: https://18656-final.slack.com

# Install

requirement:
  python: 2.7 (2.7.6 suggested)

- Install virtualenv

  pip install virtualenv

- Setup env

  virtualenv env

- Activate env

  source env/bin/activate

- Install the requirements

  pip install -r requirements.txt

# Load DBLP into Neo4j

requirement:
  maven

- Clean and Compile

  mvn clean && mvn compile

- Move dblp.xml file to 18656-final/

- Run DBLP parser

- Set Neo4j password to 123456

  http://localhost:7474/

# Run Django Web App

- Activate env

  source env/bin/activate

- Run server

  cd mysite

  python manage.py runserver

  check http://127.0.0.1:8000/

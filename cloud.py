from neo4j.v1 import GraphDatabase
import csv
class BookmarksExample():
    
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))
    def close(self):
        self._driver.close()
    
    def add_person_linkedin(self, name, email, job_type, company):
        with self._driver.session() as session:
            emp="no"
            if company=="persistent systems":
                emp="yes"
            session.run("MERGE(emp:Person {first_name: $name, email: $email, job_type: $job_type,employee:$emp})"
                          "MERGE (com: Company {name: $company})"
                          "MERGE (emp)-[:WORKS_FOR]->(com)",
                          name=name, email = email, job_type = job_type, company = company,emp=emp)
    @staticmethod
    def match_person_nodes(tx):
        return list(tx.run("MATCH (a:Person) RETURN a.name AS name"))
    
    def add_person_crm(self,customer,employee,company,touch_point,short_term,medium_term,long_term):
        with self._driver.session() as session:
            empY="yes"
            empN="no"
            compY="persistent systems"
            email=""
            job_type=""
            session.run("MERGE (empYes:Person{first_name: $employee, email: $email, job_type: $job_type,employee:$empY})"
                        "MERGE (empNo:Person{first_name: $customer,email: $email, job_type: $job_type,employee:$empN})"
                        "MERGE (empYes)-[:CONNECTED{touch_point:$touch_point,s_term:$s_term,m_term:$m_term,l_term:$l_term}]->(empNo)"
                        "MERGE (comYes: Company {name: $compY})"
                        "MERGE (empYes)-[:WORKS_FOR]->(compYes)"
                        "MERGE (compNo:Company {name: $compN})"
                        "MERGE (empNo)-[:WORKS_FOR]->(compNo)",
                        employee=employee,customer=customer,empY=empY,empN=empN,
                        touch_point=touch_point,compY=compY,compN=company,
                        email=email,job_type=job_type,s_term=short_term,m_term=medium_term,l_term=long_term)
            
uri = "bolt://localhost:7687"
book = BookmarksExample(uri, "neo4j", "pooja")

with open('Linked contacts - SavedContactList.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\t')
    next(readCSV, None)
    for row in readCSV:
        book.add_person_linkedin(row[0],row[1],row[3],row[2])
        
with open('CRM Data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\t')
    next(readCSV, None)
    for row in readCSV:
        book.add_person_crm(row[0],row[2],row[3],row[4],row[5],row[6],row[7])
        
with open('Meta data file - Role Vs offerings.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV, None)
    for row in readCSV:
        book.add_person_meta(row[0],row[1])
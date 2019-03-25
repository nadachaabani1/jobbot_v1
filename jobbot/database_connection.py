import datetime
import psycopg2
import json
from bson import json_util
import time

host = "localhost"
database ="kadir_test_01"
user = "postgres"
password = "HaqCGB8KBE"

class ConnectionAPI(object):  
    def connection(self,date,job,competency,degree_level):

        """ Connect to the PostgreSQL database server """
        conn = None
        
        try:
            listJob = list()
            # connect to the PostgreSQL server
            conn = psycopg2.connect(host=host,database=database, user=user, password=password)
            print('Connecting to the PostgreSQL database...')
            print("listJob should be empty : "+str(listJob))
            
            # create a cursor
            cur = conn.cursor()

            # execute a statement
            q= r"""select job.id , COUNT(job.id) AS num
            from job, job_competency , competency , degree_level where
            job.is_publish = true and
            applied_before >= '{0}' and
            ( lower(job_title) like {1} ) and 
            job.id = job_competency.job_id and
            job_competency.competency_id = competency.id and
            ( lower(competency_title) in {2} ) and 
            job.degree_id = degree_level.id and
            (lower(degree_name) like '%{3}%' )
            group by (job.id)
            order by COUNT(job.id) desc""".format(date,job,competency,degree_level)

            print("Query : \n")
            print(q)

            cur.execute(q)
            rows = cur.fetchall()
            print("\n")
            for row in rows: 
                jobID = {
                    "job_id":row[0],
                    "num":row[1]      
                }

                query = r""" select job.id , job.job_title ,company."name" , job.posting_date , job.applied_before , 
                degree_level.degree_name ,career_level.career_level, min_experience, currency_salary , primary_location ,
                job.job_description , competency_title
                from job , company , degree_level , career_level, job_competency , competency where
                job.id = {0} and
                job.company_id = company.id and
                job.degree_id = degree_level.id and 
                job.career_level_id = career_level.id and
                job.id = job_competency.job_id and
                job_competency.competency_id = competency.id
                """.format(jobID['job_id'])
                
                print("Query for id =  " + str(jobID['job_id']))
                print(query)
                    
                cur.execute(query)
                rows1 = cur.fetchall()
                firstRow = rows1[0]
                competencyList = [firstRow[11]]
                job = {
                        "job_id" : firstRow[0], 
                        "job_title" : firstRow[1], 
                        "company" :firstRow[2],
                        "posting_date" : int(time.mktime(firstRow[3].timetuple())),
                        "applied_before":int(time.mktime(firstRow[4].timetuple())),
                        "degree_level" : firstRow[5],
                        "career_level" : firstRow[6],
                        "experience" : firstRow[7],
                        "salary" : firstRow[8],
                        "location" : firstRow[9],
                        "job_description" : firstRow[10]
                } 
                for row in rows1[1:] :
                    competencyList.append(row[11])

                job.update({"compentency":competencyList})
                    
                print(str(job))
                listJob.append(json.dumps(job))          
            cur.close()
            
            print("listJob after query : "+ str(listJob))
            print("\n")
            return listJob
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error) 
        finally:
            if conn is not None:
                conn.close()  

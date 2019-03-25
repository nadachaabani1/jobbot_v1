from json import JSONEncoder
import time
class Job(JSONEncoder):
    def __init__(self,job_id,job_title,company,posting_date,applied_before,degree_level,career_level,experience,salary,location,job_description,competency):
        self.job_id = job_id
        self.job_title = job_title
        self.company = company
        self.posting_date = int(time.mktime(posting_date.timetuple()))
        self.applied_before = int(time.mktime(applied_before.timetuple()))
        self.degree_level = degree_level
        self.career_level = career_level
        self.experience = experience
        self.salary = salary
        self.location = location
        self.job_description = job_description
        self.competency = competency

    def __repr__(self):
        return str({
        'job_id':self.job_id, 
        'job_title':self.job_title, 
        'company':self.company,
        'posting_date':self.posting_date,
        'applied_before':self.applied_before,
        'degree_level':self.degree_level,
        'career_level':self.career_level,
        'experience':self.experience,
        'salary':self.salary,
        'location':self.location,
        'job_description':self.job_description,
        'competency':self.competency
        })
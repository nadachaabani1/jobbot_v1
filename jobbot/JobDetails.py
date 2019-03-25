from json import JSONEncoder
import time
class JobDetails(JSONEncoder):
    def __init__(self,job_id,job_title,applied_before,num):
        self.job_id = job_id
        self.job_title = job_title
        self.applied_before = int(time.mktime(applied_before.timetuple()))
        self.num = num

    def __repr__(self):
        return str({'job_id':self.job_id, 'job_title':self.job_title, 'applied_before':self.applied_before, 'num':self.num})
    '''
    class Person():

    def __init__(self, id_person, first_name, last_name, age, sex, income):
        self.id_person = id_person
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.income = income

    def __str__(self):
        return (f'ID: {self.id_person}, '
                f'First name: {self.first_name}, '
                f'Last name: {self.last_name}, '
                f'Age: {self.age}, '
                f'Sex: {self.sex}, '
                f'Income: {self.income}')
    '''                
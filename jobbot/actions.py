# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from database_connection import ConnectionAPI
import datetime
import psycopg2
import database_connection



pathOut = "action search job.txt"
writeFile = open(pathOut, "w+",encoding="utf8")

class ActionSearchJobs(Action):
    def name(self):
        """Unique identifier of the form"""
        return 'action_search_jobs'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("looking for jobs")
        
        #job_api = JobAPI()
        #jobs = job_api.search(tracker.get_slot("job_title"))

        job = tracker.get_slot('job_title')
        print("job title slot : "+job)
        print("\n")

        title = job.lower().split(' ')
        job_title="'%" + "%' or lower(job_title) like '%".join(title) + "%'"
        print("job title : "+job_title)
        print("\n")

        comp = tracker.get_slot('competency')
        print("competence slot: "+str(comp))
        print("\n")

        c= list(map(lambda x: x.lower(), comp))
        competency="('" + "') or lower(competency_title) in ('".join(c) + "')"
        print("competency : "+competency)
        print("\n")

        degree_name = tracker.get_slot('degree_name')
        print("degree_name slot : "+degree_name)
        print("\n")

        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("date : "+str(date))
        print("\n")

        # Connect to the PostgreSQL database server
        #listJob = database_connection.connection(date,job_title,competency,degree_name)

        dispatcher.utter_message("We have a position where that could work out well :" )  
        connection_api = ConnectionAPI()
        listJob = connection_api.connection(date,job_title,competency,degree_name) 
       
        print("listJob in action: "+str(listJob)) 
        print("\n")

        if (len(listJob) == 0 ):
            listJob = ["No job match found"]
            
        return [SlotSet("matches", value=listJob)]

class ActionGetMatch(Action):
    def name(self):
        return 'action_get_jobs'

    def run(self, dispatcher, tracker, domain):
        job = tracker.get_slot("matches")
        dispatcher.utter_message(str(job))
        return []

class ActionSuggest(Action):
    def name(self):
        return 'action_suggest'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what I found:")
        dispatcher.utter_message(tracker.get_slot("matches"))
        dispatcher.utter_message("is it ok for you? "
                                 "hint: I'm not going to "
                                 "find anything else :)")
        return []

from locust import HttpUser, task, TaskSet
from common.auth import login

class WebsiteUser1(TaskSet):

    @task
    def login(self):
        # GET login page to get csrftoken from it
        print("logging innnnnnnnnn admin")
        response = self.client.get('quiz/login/')
        csrftoken = response.cookies['csrftoken']
        # POST to login page with csrftoken
        self.client.post('quiz/login/',
                            {'username': 'admin', 'password': 'admin'}, 
                            headers={'X-CSRFToken': csrftoken})

    # def on_start(self):
    #     self.login()

    # def login(self):
    #     # GET login page to get csrftoken from it
    #     response = self.client.get('quiz/login/')
    #     csrftoken = response.cookies['csrftoken']
    #     # POST to login page with csrftoken
    #     self.client.post('quiz/login/',
    #                      {'username': 'prajaip', 'password': 'locust'}, 
    #                      headers={'X-CSRFToken': csrftoken})

    @task(1)
    def index(self):
        self.client.get('quiz/home/1')

    @task(1)
    def get_people(self):
        self.client.get('quiz/get/1/')
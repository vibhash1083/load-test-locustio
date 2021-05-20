from locust import HttpUser, task, TaskSet
from common.auth import login

class WebsiteUser2(TaskSet):

    # def on_start(self):
    #     self.login()
    @task
    def login(self):
    # GET login page to get csrftoken from it
        print("logging innnnnnnnnn prajaip")
        response = self.client.get('quiz/login/')
        csrftoken = response.cookies['csrftoken']
        # POST to login page with csrftoken
        self.client.post('quiz/login/',
                            {'username': 'admin1', 'password': 'admin1'}, 
                            headers={'X-CSRFToken': csrftoken})

    @task(1)
    def index(self):
        self.client.get('quiz/home/1')

    @task(1)
    def get_people(self):
        self.client.get('quiz/get/1/')
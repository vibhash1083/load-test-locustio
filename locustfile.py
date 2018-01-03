# locustfile.py
from locust import HttpLocust, TaskSet, task
import json
import datetime
import requests

class UserBehavior(TaskSet):

    def on_start(self):
        self.login()

    def login(self):
        # GET login page to get csrftoken from it
        response = self.client.get('/accounts/login/')
        csrftoken = response.cookies['csrftoken']
        # POST to login page with csrftoken
        self.client.post('/accounts/login/',
                         {'username': 'suser', 'password': 'asdf1234'}, 
                         headers={'X-CSRFToken': csrftoken})

    @task(1)
    def index(self):
        self.client.get('/')

    @task(2)
    def get_campaign(self):
        self.client.get('/5/campaign/')

    # @task(3)
    # def get_stats(self):
    #     # ajax GET
    #     self.client.get('/5/clientstats/',
    #     headers={'X-Requested-With': 'XMLHttpRequest'})

    @task(3)
    def get_advertiser_api(self):
        auth_response = self.client.post('/auth/login/', {'username': 'suser', 'password': 'asdf1234'})
        auth_token = json.loads(auth_response.text)['token']
        jwt_auth_token = 'jwt '+auth_token
        adv_api_response = self.client.get('/api/advertiser/', headers={'Authorization': jwt_auth_token})
        print("Adv API reponse ", adv_api_response.text)

    @task(4)
    def add_advertiser_api(self):
        auth_response = self.client.post('/auth/login/', {'username': 'suser', 'password': 'asdf1234'})
        auth_token = json.loads(auth_response.text)['token']
        jwt_auth_token = 'jwt '+auth_token
        now = datetime.datetime.now()
        
        current_datetime_string = now.strftime("%B %d, %Y")
        adv_name = 'locust_adv' 
        data = {'name', current_datetime_string}
        adv_api_response = requests.post('http://127.0.0.1:8000/api/advertiser/', data, headers={'Authorization': jwt_auth_token})
        
class WebsiteUser(HttpLocust):
    task_set = UserBehavior

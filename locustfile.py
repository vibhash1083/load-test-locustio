# locustfile.py
from locust import HttpUser, TaskSet, task
import json
import datetime
import requests
from locustfiles.test1 import WebsiteUser1
from locustfiles.test2 import WebsiteUser2

from locust import HttpUser, events

class WebsiteUser1(HttpUser):
    tasks = [WebsiteUser1, WebsiteUser2]
    


# PACKAGE_PARENT = '..'
# SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
# sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# from .test1 import WebsiteUser1




# class UserBehavior(TaskSet):

#     def on_start(self):
#         self.login()

#     def login(self):
#         # GET login page to get csrftoken from it
#         response = self.client.get('/accounts/login/')
#         csrftoken = response.cookies['csrftoken']
#         # POST to login page with csrftoken
#         self.client.post('/accounts/login/',
#                          {'username': 'suser', 'password': 'asdf1234'}, 
#                          headers={'X-CSRFToken': csrftoken})

#     @task(1)
#     def index(self):
#         self.client.get('/')

#     @task(2)
#     def get_campaign(self):
#         self.client.get('/5/campaign/')

#     # @task(3)
#     # def get_stats(self):
#     #     # ajax GET
#     #     self.client.get('/5/clientstats/',
#     #     headers={'X-Requested-With': 'XMLHttpRequest'})

#     @task(3)
#     def get_advertiser_api(self):
#         auth_response = self.client.post('/auth/login/', {'username': 'suser', 'password': 'asdf1234'})
#         auth_token = json.loads(auth_response.text)['token']
#         jwt_auth_token = 'jwt '+auth_token
#         adv_api_response = self.client.get('/api/advertiser/', headers={'Authorization': jwt_auth_token})
#         print("Adv API reponse ", adv_api_response.text)

#     @task(4)
#     def add_advertiser_api(self):
#         auth_response = self.client.post('/auth/login/', {'username': 'suser', 'password': 'asdf1234'})
#         auth_token = json.loads(auth_response.text)['token']
#         jwt_auth_token = 'jwt '+auth_token
#         now = datetime.datetime.now()
        
#         current_datetime_string = now.strftime("%B %d, %Y")
#         adv_name = 'locust_adv' 
#         data = {'name', current_datetime_string}
#         adv_api_response = requests.post('http://127.0.0.1:8000/api/advertiser/', data, headers={'Authorization': jwt_auth_token})

# class WebsiteUser(HttpUser):

#     def on_start(self):
#         self.login()

#     def login(self):
#         # GET login page to get csrftoken from it
#         response = self.client.get('quiz/login/')
#         csrftoken = response.cookies['csrftoken']
#         # POST to login page with csrftoken
#         self.client.post('quiz/login/',
#                          {'username': 'prajaip', 'password': 'locust'}, 
#                          headers={'X-CSRFToken': csrftoken})

#     @task(1)
#     def index(self):
#         self.client.get('quiz/home/1')

#     @task(1)
#     def get_people(self):
#         self.client.get('quiz/get/1/')

    # @task(2)
    # def get_starships(self):
    #     self.client.get('/api/starships/9/')


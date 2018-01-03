# Load testing Dajngo applications using LocustIO

Django framework, used for buliding web applications quickly in a clean and efficient manner. As the size of application increases, a common issue faced by all teams is performance of the application. Measuring performance and analysis the areas of improvement is key to deliver a quality product.


[LocustIO](https://github.com/locustio/locust), an open source tool written in python, is used for [load testing](https://en.wikipedia.org/wiki/Load_testing) of web applications. It is simple and easy to use with web UI to view the test results. It is scalable and can be distributed over multiple machines. 

This article demonstrates an example to use locust for load testing of our django web application. 

Before starting load testing, we have to decide the pages which we want to test. In our case, we expect users to follow the scenario where they log in, visit different pages and submit CSRF protected forms.

LocustIO helps us in emulating the users performing these tasks on our web application. Basic idea of measuring the performance is make number of request for different tasks and analysis the success and failure of those requests. 


##### Installation

```
pip install locustio
```

LocustIO supports python 2.x only. Currently there is no support for python 3.x.


### Locust File
Locust file is created to simulate the actions of users of the web applications. 

```
# locustfile.py
from locust import HttpLocust, TaskSet, task

class UserActions(TaskSet):

    def on_start(self):
        self.login()

    def login(self)
        # login to the application
        response = self.client.get('/accounts/login/')
        csrftoken = response.cookies['csrftoken']
        self.client.post('/accounts/login/',
                         {'username': 'username', 'password': 'password'}, 
                         headers={'X-CSRFToken': csrftoken})

    @task(1)
    def index(self):
        self.client.get('/')

    for i in range(4):
        @task(2)
        def first_page(self):
            self.client.get('/list_page/')
       
    
    @task(3)
    def get_second_page(self):
        self.client.('/create_page/', {'name': 'first_obj'}, headers={'X-CSRFToken': csrftoken})
        
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
        
        
    class ApplicationUser(HttpLocust):
        task_set = UserActions
        min_wait = 0
        max_wait = 0
```

In above example, locust file defines set of 4 tasks performed by the user - navigate to home page after login, visiting list page multiple times and submitting a form once.

Parameters, min_wait and max_wait, define the wait time between different user requests.


### Run Locust

Navigate to the directory of locustfile.py and run

```
locust --host=<host_name>
```
where <host_name> is the URL of the application

Locust instance runs locally at http://127.0.0.1:8089 

When a new test is started, locust web UI prompts to enter number of users to simulate and hatch rate(number of users per second).


We first try to simulate 5 users with hatch rate of 1 user per second and observe the results

![](images/locust_users.png)

Once a test is started, locustIO executes all tasks and results of success/failure of requests are recorded. These results are displayed in the format shown below:

![](images/locust_exe2.png)

As seen from the example above, there is one login request and multiple requests to get a page and submit a form. Since the number of users is less there is no failover.

Now let us increase the number of requests to 1000 users with hatch rate of 500 and see the results

![](images/locust_user2.png)

![](images/locust_exe4.png)

As we can that some of the requests for fetching the homepage and posting the form fail in this scenario as the number of users and requests increase. With current set of simulated users, we get failure rate of 7%. 

Observations:
1. Most of the failures are in login. Some of the failures stem from the fact that application prevents multiple login from same account in short interval of time.
2. Get request for pages has very low failure rate - 3%
3. Post requests have lower failure rates of less than 2%

We can perform multiple tests for different range of users and with the test results, it can be identified under how much stress the application is capable of performing.

The result produces following data for tests

1. Type of requests - related to each task to be simulated
2. Name - Name of the task/request
3. Number of requests - Total number of requests for a task
4. Number of failures - Total number of failed requests
5. The median, average, max and min of requests in milliseconds
6. Content size - Size of requests data
7. Request per second

We can see the details of failed requests in Failures tab which can be used to indetify the root cause of recurring failures.

![](images/locust_failures.png)

LocustIO provides option to download the results in sheets, however there is no out of the box result visualization feature in form of graphs or charts. 

Load tests results can be viewed in JSON format at ```http://localhost:8089/stats/requests```. These requests can be used as input for data visualization using different tools like Tableau, matplotlib etc.

Thus we are able to determine the system performance at different endpoints in very simple and efficient way. We can expand tests to add more scenarios for more endpoints and quickly get the answers.

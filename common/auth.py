def login(self):
    # GET login page to get csrftoken from it
    print("logging innnnnnnnnn")
    response = self.client.get('quiz/login/')
    csrftoken = response.cookies['csrftoken']
    # POST to login page with csrftoken
    self.client.post('quiz/login/',
                        {'username': 'prajaip', 'password': 'locust'}, 
                        headers={'X-CSRFToken': csrftoken})
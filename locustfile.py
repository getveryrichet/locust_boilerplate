from locust import FastHttpUser, task

headers = {
    
}

class MyUser(FastHttpUser):
    @task
    def homepage(self):
        self.client.get('/', name="test", headers=headers)
import requests
import time

class Capsolver:
    def __init__(self, API_KEY):
        self.api_key = API_KEY

    def balance(self):
        res = requests.post("https://api.capsolver.com/getBalance", json={
            "clientKey": self.api_key
        })
        return res.json()["balance"]
    
    def create_recap_v2_task(self, site_key, url):
        res = requests.post("https://api.capsolver.com/createTask", json={
            "clientKey": self.api_key,
            "task": {
                "type": "ReCaptchaV2Task",
                "websiteURL": url,
                "websiteKey": site_key
            }
        })
        return res.json()
    
    def get_task_result(self, task_id):
        res = requests.post("https://api.capsolver.com/getTaskResult", json={
            "clientKey": self.api_key,
            "taskId": task_id
        })
        return res.json()
    
    def solve_recap_v2(self, site_key, url):
        task = self.create_recap_v2_task(site_key, url)
        task_id = task["taskId"]

        while True:
            time.sleep(1)
            result = self.get_task_result(task_id)
            if result["status"] == "ready":
                return result["solution"]
            elif result["status"] == "processing":
                pass
            else:
                raise Exception("Task failed")

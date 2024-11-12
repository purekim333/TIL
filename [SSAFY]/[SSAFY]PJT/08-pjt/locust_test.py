from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)

    # 가상 유저 생성 시 자동으로 호출되는 메서드
    def on_start(self):
        print('test start')

    @task
    def average_age(self):
        self.client.get("age/")
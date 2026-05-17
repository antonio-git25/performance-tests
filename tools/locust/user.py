from locust import User, between


class LocustBaseUser(User):
    host = "localhost"
    abstract = True
    wait_time = between(1, 3)
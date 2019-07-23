import os


class Environment:
    host = None
    project = None
    job = None
    step = None

    def __init__(self):
        self.host = os.environ.get('CONTIFLOW_HOST')
        self.project = os.environ.get('CONTIFLOW_PROJECT')
        self.job = os.environ.get('CONTIFLOW_JOB')
        self.step = os.environ.get('CONTIFLOW_STEP')

    def get_base_url(self):
        return self.host + "/api"

    def get_project(self):
        return self.project

    def get_job(self):
        return self.job

    def get_step(self):
        return self.step

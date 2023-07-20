class human(object):
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getJob(self):
        return self.job
    
    def __str__(self) -> str:
        pass
    

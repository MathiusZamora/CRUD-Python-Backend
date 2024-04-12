class City:
    def __init__(self, name, status, id):
        self.name = name
        self.status = status
        self.id = id
        

    def __str__(self):
        return self.name
    
class Job:
    def __init__(self, name, status, id):
        self.name = name
        self.status = status
        self.id = id

    def __str__(self):
        return self.name
    
class Employee:
    def __init__(self, nombre, ciudad_id, job_id, salary, status, id):
        self.nombre = nombre
        self.ciudad_id = ciudad_id
        self.job_id = job_id
        self.salary = salary
        self.status = status
        self.id = id
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_city(self):
        return self.city.name
    
    def get_job(self):
        return self.job.name
    
    def get_salary(self):
        return self.salary
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status

    

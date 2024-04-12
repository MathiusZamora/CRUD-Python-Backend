import mysql.connector

class Connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None
        self.connect()
        
    def connect(self):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)

    def close(self):
        self.cnx.close()

    def execute_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        self.cnx.commit()
        cursor.close()
        return cursor

    def execute_read_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result
    
class DaoCity:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all(self):
        query = 'SELECT * FROM cities'
        return self.connection.execute_read_query(query, ())
    
    def get_by_id(self, id):
        query = 'SELECT * FROM cities WHERE name = %s'
        return self.connection.execute_read_query(query, (id,))
    
    def insert(self, city):
        query = 'INSERT INTO cities (name, status) VALUES (%s, %s)'
        return self.connection.execute_query(query, (city.name, city.status))
    
    def update(self, city):
        query = 'UPDATE cities SET name = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (city.name, city.status, city.id))
    
    def delete(self, id):
        query = 'DELETE FROM cities WHERE id = %s'
        return self.connection.execute_query(query, (id,))
    
class DaoJob:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all(self):
        query = 'SELECT * FROM jobs'
        return self.connection.execute_read_query(query, ())
    
    def get_by_id(self, id):
        query = 'SELECT * FROM jobs WHERE name = %s'
        return self.connection.execute_read_query(query, (id,))
    
    def insert(self, jobs):
        query = 'INSERT INTO jobs (name, status) VALUES (%s, %s)'
        return self.connection.execute_query(query, (jobs.name, jobs.status))
    
    def update(self, jobs):
        query = 'UPDATE jobs SET name = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (jobs.name, jobs.status, jobs.id))
    
    def delete(self, id):
        query = 'DELETE FROM jobs WHERE id = %s'
        return self.connection.execute_query(query, (id,))
    
class DaoEmployee:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all(self):
        query = """
        SELECT 'ID', 
           'Nombre', 
           'Ciudad', 
           'Trabajo', 
           'Salario', 
           'Estado'
        UNION ALL
        SELECT employees.id, 
           employees.nombre AS Nombre, 
           cities.name AS ciudad, 
           jobs.name AS Trabajo, 
           employees.salary,  
           employees.status
        FROM employees
        JOIN cities ON employees.ciudad_id = cities.id
        JOIN jobs ON employees.job_id = jobs.id;
        """
        return self.connection.execute_read_query(query, ())
    
    def get_by_id(self, id):
        query = 'SELECT * FROM employees WHERE nombre = %s'
        return self.connection.execute_read_query(query, (id,))
    
    def insert(self, employees):
        query = 'INSERT INTO employees (nombre, ciudad_id, job_id, salary, status) VALUES (%s, %s, %s, %s, %s)'
        return self.connection.execute_query(query, (employees.nombre, employees.ciudad_id, employees.job_id, employees.salary, employees.status))
    
    def update(self, employees):
        query = 'UPDATE employees SET nombre = %s, ciudad_id = %s, job_id = %s, salary = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (employees.nombre, employees.ciudad_id, employees.job_id, employees.salary, employees.status, employees.id))
    
    def delete(self, id):
        query = 'DELETE FROM employees WHERE id = %s'
        return self.connection.execute_query(query, (id,))
    
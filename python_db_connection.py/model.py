class Employee:

    def insert(self,id,name,dept,salary):
        self.eid=id
        self.ename=name
        self.edept =dept
        self.esalary = salary

    def get_id(self):
        return self.eid
        
    def get_name(self):
        return self.ename

    def get_dept(self):
        return self.edept
    
    def get_salary(self):
        return self.esalary
        
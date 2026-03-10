class Employee:
    def __init__(self, first_name, last_name, emp_id, perms, salary):
        self.firstname = first_name
        self.lastname = last_name
        self.id = emp_id
        self.permlevel = perms
        self.salary = salary
    
    def get_info(self):
        print(f'Name: {self.firstname} {self.lastname}')
        print(f'ID: {self.id}')
        print(f'Permissions: {self.permlevel}')
        print(f'Salary: {self.salary}')
    
    def get_name(self):
        print(f'{self.firstname} {self.lastname}')

    def get_id(self):
        print(self.id)
    
    def get_job(self):
        print(self.permlevel)
    
    def get_salary(self):
        print(self.salary)

    def give_raise(self, raise_amnt):
        self.salary += raise_amnt


emp1 = Employee('Joseph', 'Jerstad', 'A001', 'Admin', 85000)

emp1.give_raise(5000)

emp1.get_info()



    
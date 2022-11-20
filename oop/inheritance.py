import numbers


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show_data(self):
        print(self.name)
        print(self.age)

    def show_details(self):
        print(f'My name is: {self.name}')
        print(f'My age: {self.age}')


class Employee(Person):
    def __init__(self, name: str, age: int, salary: numbers, post: str):
        Person.__init__(self, name, age)
        self.salary = salary
        self.post = post

    def show_details(self):
        print(f'My name is: {self.name}')
        print(f'My age: {self.age}')
        print('Post: {}'.format(self.post))


employee = Employee(name='Pepito', age=35, salary=400, post='Old post in article')
employee.show_data()
employee.show_details()


"""
 Desc:
  Multiple Inheritance
  Use case DB modeling
"""


class TeamMember:
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid


class Worker:
    def __init__(self, job_title, salary):
        self.job_title = job_title
        self.salary = salary


class TeamLeader(TeamMember, Worker):
    def __init__(self, name, uid, job_title, salary, experience_time):
        self.name = name
        self.uid = uid
        self.job_title = job_title
        self.salary = salary
        self.experience_time = experience_time
        TeamMember.__init__(self, name, uid)
        Worker.__init__(self, job_title, salary)


team_leader = TeamLeader(name='Sara', uid=1, job_title='Software Engineer', salary=1500, experience_time=2)

"""
 Desc:
  Python program to demonstrate how MRO works
  in multiple inheritance
"""


class Agile:
    def create(self):
        print(" Forming class Agile")


class Dev(Agile):
    def create(self):
        print(" Forming class Dev")


class QA(Agile):
    def create(self):
        print(" Forming class QA")


class Sprint(Dev, QA):
    pass


sprint = Sprint()
sprint.create()
print(Sprint.__mro__)

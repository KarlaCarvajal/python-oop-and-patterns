class Company:
    # private class attribute
    __benefits: str

    def __init__(self, schedule):
        # protected instance attribute
        self._project = "ADAMS"
        # private instance attribute
        self.__schedule = schedule

    def get_benefits(self):
        return self.__benefits

    def set_benefits(self, benefits):
        self.__benefits = benefits

    def get_schedule(self):
        return self.__schedule


class Employee(Company):
    def __init__(self, name, salary, schedule):
        self.name = name
        self.__salary = salary
        Company.__init__(self, schedule)

    def show_data(self):
        print(f'Employee {self.name} is participating in {self._project} project on schedule {self.get_schedule()}')


company_formal_schedule = 'Monday to Friday from 9:00 to 18:00'
company = Company(company_formal_schedule)
company.set_benefits('Monthly budget for learning')
print(f'The benefits for the company are: {company.get_benefits()}')
employee = Employee(name='Thom', salary=400, schedule=company_formal_schedule)
employee.show_data()





class Employee:
    def __init__(self, name, salary, on_vacation ):

        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation

employees = [
    Employee('Данил', 500),
    Employee('Иван', 400),
    Employee('Кирилл', 450)
]
 
for emp in employees:
    print(f'У {emp.name}а зарплата в год составляет {emp.salary*12} руб. Отпуск {emp.on_vacation}')
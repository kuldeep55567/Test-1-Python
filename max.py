employees =[
     {"name":"John","salary":3000,"designation":"developer"},
     {"name":"Emma","salary":4000,"designation":"manager"},
     {"name":"Kelly","salary":3500,"designation":"tester"},
]
def max_salary_employee(employees):
    max_salary = 0
    employee = None
    for i in employees:
        salary = i.get("salary",0)
        if salary > max_salary:
            max_salary = salary
            employee  = i
    return employee 


print(max_salary_employee(employees))
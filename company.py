class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details (self):
        print(f'emp_name{self.emp_name}')
        print(f'emp_id{self.emp_id}')
        print(f'emp_salary{self.emp_salary}')
        print(f'emp_department{self.emp_department}')

    def calculate_emp_salary():
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (self.emp_salary/50))
            total_salary = overtime_amount = self.emp_salary
        else:
            total_salary = self.emp_salary
        return total_salary
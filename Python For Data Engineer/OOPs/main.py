class Employee:
    company_name = "XYZ"

    def __init__(self, emp_name, emp_dept) -> None:
        self.emp_name = emp_name
        self.emp_dept = emp_dept

    @property
    def info(self):
        return f"Employee {self.emp_name} is working in department: {self.emp_dept} for company: {self.company_name}"

    @info.setter
    def info(self, value):
        if isinstance(value, list) and len(value) == 2:
            self.emp_name = value[0]
            self.emp_dept = value[1]
        else:
            raise ValueError("Please provide a list with [name, department]")

    @staticmethod
    def add(p_x, p_y):
        print(p_x + p_y)

    @classmethod
    def changesInClass(cls, new_company):
        cls.company_name = new_company


emp1 = Employee("Samiran", "IT")
emp2 = Employee("Rahul", "Support")

emp1.changesInClass("SCT")  # Changes company for all instances
emp1.info = ["Joy", "HR"]   # Updates emp1 name and department
print(emp1.info)            # Prints updated info

emp1.add(10, 10)            # Uses static method

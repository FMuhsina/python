class Employee:
    company_name="infosys"
    location="Calicut"
    def __init__(self, id, name, salary):
        self.emp_id = id
        self.emp_name = name
        self.emp_salary = salary

    def display_details(self):
        print("Eployee Id: ",self.emp_id)
        print("Eployee Name: ",self.emp_name)
        print("Color: ",self.emp_salary)
        print("-" * 30)

# Create instances of Car
emp1 = Employee("101", "Muhsina", 25000)
emp2 = Employee("102", "Henna", 28000)
emp3 = Employee("103", "Adhila", 35000)

# Display car details
emp1.display_details()
emp2.display_details()
emp3.display_details()

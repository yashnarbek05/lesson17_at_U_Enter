from Date import Date
from Employee import Employee
from Phone import Phone
from Vehicle import Car

if __name__ == '__main__':
    phone = Phone("blue", 1200)
    employee = Employee("Tony", 19, 2300,"Male")

    print(phone)
    print(employee)
    employee.employee_details()

    car = Car(1200, 200)
    print(car)

    date = Date(2000,10,31)
    print(date)
    date.show_time()
# Section 1: Classes and Objects (1–10)

# 1. Create a Car class with attributes: brand, model, and price. Instantiate two cars and print details.

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ₹{self.price}")


car1 = Car("Toyota", "Corolla", 20000)
car2 = Car("Tesla", "Model 3", 35000)

car1.display_info()
car2.display_info()




# 2. Create a BankAccount class with methods for deposit, withdraw, and balance check.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")


account = BankAccount("Alice")
account.deposit(500)
account.withdraw(150)
account.check_balance()


# 3. Create a Student class with instance variables name, age, and grade. Accept data through the constructor.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


student1 = Student("John", 17, "A")
print(student1.name, student1.age, student1.grade)



# 4. Create a Circle class with method to calculate area and circumference.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


circle = Circle(5)
print("Area:", circle.area())
print("Circumference:", circle.circumference())



# 5. Create a Book class with display_info() method and access data via object.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Book: {self.title} by {self.author}")


book = Book("1984", "George Orwell")
book.display_info()




# 6. Create a Laptop class with class variable warranty_period shared among all objects.

class Laptop:
    warranty_period = 2  

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


laptop1 = Laptop("Dell", "Inspiron")
laptop2 = Laptop("HP", "Pavilion")
print(laptop1.warranty_period, laptop2.warranty_period)



# 7. Create a Movie class where each instance tracks the total number of movies using a class variable.

class Movie:
    count = 0 

    def __init__(self, title):
        self.title = title
        Movie.count += 1


m1 = Movie("Interstellar")
m2 = Movie("Inception")
print("Total movies:", Movie.count)




# 8. Create a Product class and demonstrate how instance variables differ from class variables.

class Product:
    category = "General"  

    def __init__(self, name, price):
        self.name = name    
        self.price = price    


p1 = Product("Pen", 2)
p2 = Product("Notebook", 5)
print(p1.name, p1.price, p1.category)
print(p2.name, p2.price, p2.category)



# 9. Implement __str__ in a class Employee to display employee data in readable format.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} works as {self.position}"


emp = Employee("Sara", "Developer")
print(emp)



# 10. Write a program to compare two Rectangle objects using __eq__ method.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


r1 = Rectangle(4, 5)
r2 = Rectangle(4, 5)
r3 = Rectangle(3, 5)
print(r1 == r2)  
print(r1 == r3)  

# Section 2: Inheritance (11–20)

# 11. Create a Vehicle class and inherit it in Car, Bike, and Truck classes.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print(f"Vehicle Brand: {self.brand}")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class Truck(Vehicle):
    pass


c = Car("Toyota")
b = Bike("Yamaha")
t = Truck("Volvo")

c.display()
b.display()
t.display()



# 12. Use super() to call the parent class constructor from a child class.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle constructor called for {brand}")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Calls parent constructor
        self.model = model
        print(f"Car model: {self.model}")


car = Car("Honda", "Civic")


# 13. Create a Shape class and derive Square and Triangle. Override an area() method.

#Method Overriding:

class Shape:
    def area(self):
        print("Area not defined")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


s = Square(4)
t = Triangle(5, 6)

print("Square area:", s.area())
print("Triangle area:", t.area())



# 14. Implement Multi-level Inheritance with Person → Employee → Manager.

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department


m = Manager("Alice", 101, "Sales")
print(m.name, m.emp_id, m.department)



# 15. Demonstrate Multiple Inheritance with Father and Mother inherited by Child.

class Father:
    def skills(self):
        print("Father: Gardening, Driving")

class Mother:
    def skills(self):
        print("Mother: Cooking, Painting")

class Child(Father, Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child: Coding")


c = Child()
c.skills()



# 16. Create a Teacher class and use hierarchical inheritance for MathTeacher, ScienceTeacher.

class Teacher:
    def teach(self):
        print("Teaching...")

class MathTeacher(Teacher):
    def subject(self):
        print("Subject: Math")

class ScienceTeacher(Teacher):
    def subject(self):
        print("Subject: Science")


m = MathTeacher()
s = ScienceTeacher()

m.teach()
m.subject()

s.teach()
s.subject()



# 17. Use isinstance() to check if an object belongs to a certain class.

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Dog))     
print(isinstance(dog, Animal))  
print(isinstance(dog, object))  


# 18.Use issubclass() to verify if a class is derived from another class.

class Animal:
    pass

class Cat(Animal):
    pass

print(issubclass(Cat, Animal))  
print(issubclass(Cat, object))  
print(issubclass(Animal, Cat))  




# 19. Create a class hierarchy for an e-commerce platform using inheritance (Product → ElectronicProduct → MobilePhone).

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, warranty, brand):
        super().__init__(name, price, warranty)
        self.brand = brand


phone = MobilePhone("Smartphone", 700, "1 year", "Samsung")
print(phone.name, phone.price, phone.warranty, phone.brand)


# 20. Demonstrate method resolution order (MRO) in a multiple inheritance example.

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass


d = D()
d.show()  # MRO: D → B → C → A
print(D.__mro__)



# Section 3: Encapsulation (21–25)


# 21. Create a Student class with private attributes _name and _marks. Use getter/setter methods.

class Student:
    def __init__(self, name, marks):
        self._name = name      # "Protected" by convention
        self._marks = marks    # "Protected" by convention

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_marks(self):
        return self._marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
        else:
            print("Invalid marks. Must be between 0 and 100.")


s = Student("John", 85)
print(s.get_name())
s.set_marks(105)  
s.set_marks(95)
print(s.get_marks())



# 22. Create a BankAccount class with balance as private variable. Ensure secure access via methods.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Alice", 500)
acc.deposit(200)
acc.withdraw(1000)
print("Balance:", acc.get_balance())



# 23. Build a UserProfile class with encapsulated email, phone and provide validation in setters.

class UserProfile:
    def __init__(self, email, phone):
        self.__email = email
        self.__phone = phone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if "@" in email:
            self.__email = email
        else:
            print("Invalid email format.")

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self.__phone = phone
        else:
            print("Invalid phone number.")


user = UserProfile("test@example.com", "1234567890")
user.set_email("not-an-email")
user.set_phone("9876543210")
print(user.get_email(), user.get_phone())



# 24. Restrict direct access to salary field in a class Employee, use getters/setters.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive.")


emp = Employee("Ravi", 40000)
print("Salary:", emp.get_salary())
emp.set_salary(-5000)  # Invalid
emp.set_salary(45000)
print("Updated Salary:", emp.get_salary())



# 25. Create a Locker system where the PIN is private and can only be changed via method.

class Locker:
    def __init__(self, pin):
        self.__pin = pin  # Private PIN

    def verify_pin(self, pin):
        return self.__pin == pin

    def change_pin(self, old_pin, new_pin):
        if self.verify_pin(old_pin):
            if len(new_pin) == 4 and new_pin.isdigit():
                self.__pin = new_pin
                print("PIN changed successfully.")
            else:
                print("New PIN must be a 4-digit number.")
        else:
            print("Incorrect current PIN.")


locker = Locker("1234")
locker.change_pin("0000", "5678")  # Incorrect
locker.change_pin("1234", "567")   # Invalid new PIN
locker.change_pin("1234", "5678")  # Success

# Section 4: Abstraction (26–30)

# 26. Use abc module to define an abstract class Payment with abstract method pay().

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


payment = CreditCardPayment()
payment.pay(100)



# 27. Create an abstract class Shape with abstract method area() and concrete method describe().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("This is a geometric shape.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


c = Circle(5)
c.describe()
print("Area:", c.area())



# 28. Implement Animal abstract class with abstract speak() method. Create subclasses Dog, Cat.


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())


# 29. Create a template for Transport with abstract methods like start_engine() and stop_engine().

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Transport):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")


car = Car()
car.start_engine()
car.stop_engine()



# 30. Create a base class Appliance with abstract method power_consumption(). Subclasses: Fridge, WashingMachine.

from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def power_consumption(self):
        pass

class Fridge(Appliance):
    def power_consumption(self):
        return "Fridge consumes 150W per hour."

class WashingMachine(Appliance):
    def power_consumption(self):
        return "Washing Machine consumes 500W per hour."


f = Fridge()
w = WashingMachine()
print(f.power_consumption())
print(w.power_consumption())


# Section 5: Polymorphism (31–35)

# 31. Demonstrate method overriding with Animal base class and Dog subclass implementing speak().

class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

a = Animal()
d = Dog()

a.speak()  
d.speak()  

# 32. Use polymorphism via duck typing – write a function that calls draw() on different shape objects.

class Circle:
    def draw(self):
        print("Drawing a circle.")

class Rectangle:
    def draw(self):
        print("Drawing a rectangle.")

def render_shape(shape):
    shape.draw()  


c = Circle()
r = Rectangle()

render_shape(c)  
render_shape(r)  

# 33. Simulate method overloading using default arguments in a class Calculator.

class Calculator:
    def add(self, a=0, b=0):
        return a + b


calc = Calculator()
print("Add two numbers:", calc.add(5, 3))
print("Add one number:", calc.add(5))
print("Add no numbers:", calc.add())



# 34. Simulate overloading using *args in a class Sum that can add 2, 3 or n numbers.

class Sum:
    def add(self, *args):
        return sum(args)


s = Sum()
print("Sum of 2 numbers:", s.add(10, 20))
print("Sum of 3 numbers:", s.add(5, 15, 30))
print("Sum of many:", s.add(1, 2, 3, 4, 5))



# 35. Create a class Notification with method send(msg). Use subclasses SMS, Email, PushNotification.

class Notification:
    def send(self, msg):
        print("Sending notification:", msg)

class SMS(Notification):
    def send(self, msg):
        print(f"Sending SMS: {msg}")

class Email(Notification):
    def send(self, msg):
        print(f"Sending Email: {msg}")

class PushNotification(Notification):
    def send(self, msg):
        print(f"Sending Push Notification: {msg}")


notifications = [SMS(), Email(), PushNotification()]
for n in notifications:
    n.send("Your balance is INR 1,000.")


# Section 6: Magic (Dunder) Methods (36–40)

# 36. Override __add__() in a Vector class to allow vector addition using +.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2
print(v3)  



# 37. Override __len__() in a Playlist class to return number of songs.

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)


p = Playlist(["Song A", "Song B", "Song C"])
print("Total songs:", len(p)) 



# 38. Override __getitem__() and __setitem__() in a class that mimics a shopping cart.

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def __getitem__(self, item):
        return self.items.get(item, 0)

    def __setitem__(self, item, quantity):
        self.items[item] = quantity


cart = ShoppingCart()
cart["apples"] = 5
cart["bananas"] = 3
print("Apples in cart:", cart["apples"])    
print("Oranges in cart:", cart["oranges"])  



# 39. Override __contains__() in a custom Inventory class to check if item exists.

class Inventory:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items


inv = Inventory(["pen", "book", "eraser"])
print("pen" in inv)     
print("pencil" in inv)   




# 40. Create a class Money and implement __eq__, __gt__, __lt__ for comparing amounts.

class Money:
    def __init__(self, amount):
        self.amount = amount  

    def __eq__(self, other):
        return self.amount == other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __str__(self):
        return f"₹{self.amount}"

m1 = Money(1500)
m2 = Money(2000)

print(m1 == m2)  
print(m1 < m2)  
print(m1 > m2)   

# Section 7: Composition & Aggregation (41–45)

# 41. Create a Car class that contains an Engine object (composition).

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print("Engine started with", self.horsepower, "HP")

class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)  

    def start_car(self):
        print(f"{self.brand} car starting...")
        self.engine.start()


car = Car("Toyota", 120)
car.start_car()



# 42. Design a Library class that has a list of Book objects (aggregation).

class Book:
    def __init__(self, title):
        self.title = title

class Library:
    def __init__(self, books):
        self.books = books  

    def display_books(self):
        for book in self.books:
            print("Book:", book.title)


book1 = Book("Python Basics")
book2 = Book("OOP with Python")

library = Library([book1, book2])
library.display_books()



# 43. Create a University class containing multiple Department objects (composition).

class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.departments = [  # Composition
            Department("Computer Science"),
            Department("Physics"),
            Department("Mathematics")
        ]

    def show_departments(self):
        print(f"Departments in {self.name} University:")
        for dept in self.departments:
            print("-", dept.name)


uni = University("IIT Delhi")
uni.show_departments()



# 44. Build a Company object that aggregates many Employee instances.

class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, employees):
        self.employees = employees 

    def list_employees(self):
        for emp in self.employees:
            print("Employee:", emp.name)


e1 = Employee("Anita")
e2 = Employee("Reetha")

company = Company([e1, e2])
company.list_employees()



# 45. Create a Flight object that includes Pilot, CabinCrew, and Passenger classes.

class Pilot:
    def __init__(self, name):
        self.name = name

class CabinCrew:
    def __init__(self, name):
        self.name = name

class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self, flight_number):
        self.flight_number = flight_number
        self.pilot = Pilot("Captain Singh")
        self.cabin_crew = [CabinCrew("Riya"), CabinCrew("Amit")]
        self.passengers = [Passenger("Sneha"), Passenger("Arjun")]

    def show_manifest(self):
        print(f"Flight {self.flight_number} Manifest:")
        print("Pilot:", self.pilot.name)
        print("Cabin Crew:", ', '.join(cc.name for cc in self.cabin_crew))
        print("Passengers:", ', '.join(p.name for p in self.passengers))


flight = Flight("AI-203")
flight.show_manifest()


# Section 8: Real-World Applications (46–50)


# 46. Create a Banking System with customer, account, transaction classes using full OOP concepts.

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

class Account:
    def __init__(self, account_number, customer):
        self.account_number = account_number
        self.customer = customer
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ₹{amount}. New Balance: ₹{self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Withdrawn ₹{amount}. Remaining Balance: ₹{self.balance}"

class Transaction:
    def __init__(self, account):
        self.account = account

    def show_balance(self):
        return f"Account Balance: ₹{self.account.balance}"


cust = Customer("Amit", 101)
acc = Account("12345678", cust)
txn = Transaction(acc)

print(acc.deposit(5000))
print(acc.withdraw(2000))
print(txn.show_balance())


# 47. Develop a Quiz Application using OOP (Question, Option, Quiz classes).

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        for q in self.questions:
            ans = input(q.prompt + " ")
            if ans.lower() == q.answer.lower():
                self.score += 1
        print(f"You scored {self.score}/{len(self.questions)}")


questions = [
    Question("Capital of India? ", "Delhi"),
    Question("2 + 2 = ? ", "4"),
]
quiz = Quiz(questions)
quiz.start() 


# 48. Implement a Hotel Management System (Room, Booking, Customer classes using inheritance).

class Room:
    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price
        self.is_booked = False

class Customer:
    def __init__(self, name):
        self.name = name

class Booking(Room):
    def __init__(self, room_number, price, customer):
        super().__init__(room_number, price)
        self.customer = customer

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            return f"Room {self.room_number} booked by {self.customer.name} for ₹{self.price}"
        return "Room already booked"


cust = Customer("Sneha")
booking = Booking(101, 2500, cust)
print(booking.book_room())


# 49. Build a School Management System with Teacher, Student, Course, Grade using abstraction and polymorphism.

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def role(self):
        pass

class Student(Person):
    def role(self):
        return "Student"

class Teacher(Person):
    def role(self):
        return "Teacher"

class Course:
    def __init__(self, title):
        self.title = title

class Grade:
    def __init__(self, student, course, marks):
        self.student = student
        self.course = course
        self.marks = marks


student = Student("Ravi")
teacher = Teacher("Mrs. Sharma")
course = Course("Math")
grade = Grade(student, course, 88)

print(student.name, "-", student.role())
print(teacher.name, "-", teacher.role())
print(f"{student.name} scored {grade.marks} in {grade.course.title}")


# 50. Develop a Library System with OOP covering: borrowing, returning, searching, adding books.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b
        return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book and book.available:
            book.available = False
            return f"You borrowed '{book.title}'"
        return "Book not available"

    def return_book(self, title):
        book = self.search_book(title)
        if book:
            book.available = True
            return f"You returned '{book.title}'"
        return "Book not found"


library = Library()
library.add_book(Book("Python 101", "Guido"))
library.add_book(Book("OOP in Python", "Rossum"))

print(library.borrow_book("Python 101"))
print(library.return_book("Python 101"))

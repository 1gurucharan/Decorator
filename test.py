# def decorator(func):
    
#     def wrapper():
#         print("starting ")
#         func()
#         print("finish")
        
#     return wrapper
    


# def greet():
#     print("Hello")
    
# g=decorator(greet)
# print(g())

##-------------------------------------------------------

# def authentication(func):
#     def wrapper():
#         print("chech login")
#         func()
#         print("successfull")
#     return wrapper
        

# @authentication
# def login():
#     print("login")
    
# login()

##-------------------------------------------------------------------

# def logger(func):
#     def wrapper():
#         print(f"calling {func.__name__  }")
#         func()
#         print(f"finished {func.__name__}")
        
#     return wrapper

# @logger
# def create_user():
#     print("creating user")
    
# create_user()

##--------------------------------------------------------------------


# def logger(func):
    
#     def wrapper(*args, **kwargs):
#         print(f"calling {func.__name__  }")
#         result=func(*args, **kwargs)
        
#         return result
    
        
#     return wrapper

# @logger
# def create_user(a,b):
#     return a+b

# r=create_user(2,6)   
# print(r)

##----------------------------------------------------------------

# def uppercase(func):

#     def wrapper(*args, **kwargs):

#         result = func(*args, **kwargs)

#         return result.upper()

#     return wrapper

# @uppercase
# def get_name():
#     return "gurucharan"

# print(get_name())

#---------------------------------------------------------------------

# def check_age(func):
#     def wrapper(age):
        
#         if age<18:
#             print("access denied")
            
#             return
        
#         return func(age)
    
#     return wrapper

# @check_age
# def access_account(age):
#     print("opened account")
    
# access_account(17)

##------------------------------------------------------------


# def first(func):
#     def wrapper():
#         print("first")
#         func()
        
#     return wrapper

# def second(func):
#     def wrapper():
#         print("second")
#         func()
        
#     return wrapper

# @first
# @second
# def greet():
#     print("Hello")

##-----------------------------------------------------------

# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
                
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
            
# @repeat(6)
# def greet():
#     print("hello")
    
# greet()

##-----------------------------------------

# from functools import wraps

# def decorator(func):

#     @wraps(func)
#     def wrapper(*args, **kwargs):

#         # logic before

#         result = func(*args, **kwargs)

#         # logic after

#         return result

#     return wrapper

# @decorator
# def add(a, b):
#     """Adds two numbers."""
#     return a + b

# print(add.__name__)

##-----------------------------------------------------------------------------


# class Employee:

#     company = "ABC"

#     def __init__(self, name, salary):
#         self.name = name
#         self._salary = salary

#     @property
#     def salary(self):
#         return self._salary

#     @salary.setter
#     def salary(self, value):

#         if value < 0:
#             raise ValueError("Salary cannot be negative")

#         self._salary = value

#     @classmethod
#     def company_name(cls):
#         return cls.company

#     @staticmethod
#     def is_valid_salary(value):
#         return value >= 0
# employee=Employee("Rahul",5000)  
# print(employee.salary)
# print(Employee.company_name())
# Employee.is_valid_salary(5000)


##-----------------------------------------------------------------------


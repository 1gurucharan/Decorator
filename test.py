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


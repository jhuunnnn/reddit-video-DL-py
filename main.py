name = "Tuna"
age=3
second_age=4
price = 19.99
is_active =True



is_greater = second_age>age


print(is_greater)

score = 85

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
else:
  print("Grade: C")
  
  
status_code = 404

match status_code:
  case 200:
    print("Success")
  case 404:
    print("Not Found")
  case 500 | 502:  # Combined cases using pipe
    print("Server Error")
  case _:  # Default fallback case
    print("Unknown status")
    
    
# Function with a parameter and a default value
def greet_user(name, greeting="Hello"):
  return f"{greeting}, {name}!"


# Calling the function
message = greet_user("Tuna", "Welcome")
print(message)  # Output: Welcome, Tuna!
    
    
    
# Defining a class
class Car:
  # Constructor method to initialize attributes
  def __init__(self, brand, speed):
    self.brand = brand
    self.speed = speed

  # Method (behavior)
  def accelerate(self):
    return f"The {self.brand} is moving at {self.speed} mph."


# Creating an object (instantiation)
my_car = Car("Toyota", 60)
print(my_car.accelerate())  # Output: The Toyota is moving at 60 mph.
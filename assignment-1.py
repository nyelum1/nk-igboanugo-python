# Section 1: Variables and Types

name = "John"
age = 30
height = 6.3
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


# Section 2: User Input and Math

name = input("Please enter your name: ")
year_of_birth = input("Please enter the year you were born: ")
birth_year = int(year_of_birth)

current_year = 2026
age = current_year - birth_year

print(f"Hi, {name}! You are approximately {age} years old.")


# Section 3: Type Conversion and f-strings

num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")

num1 = float(num1)
num2 = float(num2)

product = num1 * num2

print(f"{num1} × {num2} = {product}")


# Section 4: Formatted Receipt 

item = "Wireless mouse"
price = 24.99
quantity = 2

total = price * quantity

print("===========================")
print("        RECEIPT")
print("===========================")
print(f"Item:      {item}")
print(f"Price:     ${price:.2f}")
print(f"Quantity:  {quantity}")
print("---------------------------")
print(f"Total:     ${total:.2f}")
print("===========================")


# Section 5: Mini-Project - Profile Card 

name = input("Please enter your name: ")
hometown = input("Please enter your hometown: ")
hobby = input("Please enter your favorite hobby: ")
fun_fact = input("Please enter one fun fact about yourself: ")
birth_year = int(input("Please enter the year you were born: "))

current_year = 2026
age = current_year - birth_year

print("╔══════════════════════════════╗")
print(f"      PROFILE: {name}")
print("╚══════════════════════════════╝")
print(f"Hometown:   {hometown}")
print(f"Hobby:      {hobby}")
print(f"Fun fact:   {fun_fact}")
print(f"Age:        {age}")

### 1. Password Check Program
correct_password = "your_password"
attempts = 3

while attempts > 0:
    password = input("Enter Password: ")
    if password == correct_password:
        print("Correct Password")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("Locked")
        else:
            print(f"Incorrect password, {attempts} attempts remaining.")

### 2. Name Loop Program

number = int(input("Enter a number: "))
name = input("Enter your name: ")

for _ in range(number):
    print(name)

### 3. Multiplication Table Program

while True:
    num = int(input("Enter a positive integer: "))
    if num > 0:
        break
    else:
        print("Not a positive integer.")

print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

### 4. Prime Number Check Program

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter an integer: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
```

### 5. FizzBuzz Program

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

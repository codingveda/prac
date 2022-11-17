# Program for Fibonacci numbers

# Iterative Approach
num = int(input("enter no - "))

num1, num2, count = 0, 1, 0

if (num <= 0):
    print("enter a valid number")
elif(num == 1):
    print("fibonacci series : ", num1)
else:
    print("fibonacci series (iterative) : ")
    while (count < num):
        print(num1, end=" ")
        nth = num1 + num2
        num1 = num2
        num2 = nth
        count += 1

# Recursive Approach
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

num = int(input("\nenter no - "))
print("fibonacci series (recursive) : ")
for i in range(num):
    print(fibonacci(i), end=" ")
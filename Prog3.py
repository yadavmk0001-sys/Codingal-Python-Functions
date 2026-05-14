def add(P, Q):
    return P + Q

def subtract(P, Q):
    return P - Q

def multiply(P, Q):
    return P * Q

def divide(P, Q):
    return P / Q

print("Please select the operators : ")
print("a) Add")
print("b) Subtract")
print("c) Multiply")
print("d) Divide")

choice = input("Please enter your choice(a/ b/ c/ d) : ")

num_1 = int(input("Please enter number 1 : "))
num_2 = int(input("Please enter number 2 : "))

if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))

elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))

elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))

elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))

else:
    print("Invalid operator.")
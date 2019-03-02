def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def multiply(a,b):
    return a * b

while True:
    print("1.Add\n2.Subtract\n3.Divide\n4.Multiply")
    op = int(input("Enter choice:"))

    if op == 1:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(add(a, b))
    elif op == 2:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(sub(a, b))
    elif op == 4:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(multiply(a, b))
    else:
        break

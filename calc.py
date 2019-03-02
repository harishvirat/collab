while True:
    print("1.Add\n2.Subtract\n3.Divide\n4.Multiply")
    op = int(input(Enter choice:))
    input_vals()
    if op == 1:
        print(add(a, b))
    elif op == 2:
        print(sub(a, b))
    elif op == 3:
        print(divide(a, b))
    elif op == 4:
        print(multiply(a, b))
    else:
        break

def add(a,b):
    return a+b

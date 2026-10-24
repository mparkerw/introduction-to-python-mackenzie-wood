a = float(input("First Number: "))
op = input("Operator (+ - * /): ")
b = float(input("Second Number: "))

if op == "+":
    result = a + b
    print(f"{a} {op} {b} = {result}")
elif op == "-":
    result = a - b
    print(f"{a} {op} {b} = {result}")
elif op == "*":
    result = a * b
    print(f"{a} {op} {b} = {result}")
elif op == "/":
    if b == 0:
       print("Error: division by zero")
    else: 
        result = a / b
        print(f"{a} {op} {b} = {result}")
else:
    print("Used Operator not in List", op)


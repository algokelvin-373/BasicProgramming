# Day 02 - 3. Mathematical Manipulation

a, b = 8, 3

print("Case 1: ")
print("a / b           : ", (a / b))
print("int(a / b)      : ", int(a / b))
print("round(a / b)    : ", round(a / b))
print("round(a / b, 2) : ", round(a / b, 2))
print("a // b : ", (a // b), " - type : ", type(a // b))

print("\nCase 2: ")
result = a + b  # 11
print("a + b =     ->", result)
result += b  # looks like 'result = result + b'
print("result += b ->", result)

print("\nCase 3: ")
x = 373
y = "Algokelvin"
z = True
print(f"Value x is {x} | Value y is {y} | Value z is {z}")

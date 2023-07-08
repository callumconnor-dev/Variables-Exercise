a = input("a: ")
b = input("b: ")

c = a
a = b   # Using 'c' as storage to hot-swap variables a and b without losing their values
b = c

print("a: " + a)
print("b: " + b)
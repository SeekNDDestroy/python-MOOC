from math import sqrt
a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))

term = (b ** 2 - (4 * a * c));
x = (-b + sqrt(term)) / (2 * a);
y = (-b - sqrt(term)) / (2 * a);

print(f"The roots are {x} and {y}")

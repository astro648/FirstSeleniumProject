import random

print("Generate 10 Random Numbers from 1-100")
for i in range(10):
    print(random.randint(1, 100))
print("\n")

print("Generate 10 Random Even Numbers")
counteven = 1
for counteven in range(10):
    a = random.randint(1, 100)
    if a == int(a):
        print(a)
        counteven = counteven + 1
print("\n")

print("Generate 10 Random Odd Numbers")
countodd = 1
for countodd in range(10):
    b = random.randint(1, 100)
    if b != int(b):
        print(b)
        countodd = countodd + 1
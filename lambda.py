x = lambda a: a + 10  # lambda is anonymous function without name
print(x(5))
y = lambda x,y: x * y
print(y(2,4))
Max = lambda a, b: a if (a > b) else b
print(Max(1, 2))
tables = [lambda x=x: x * 10 for x in range(1, 11)]
for table in tables:
    print(table())
sum = 0
a, b = 0, 1
while(a < 4000000):
    a, b = b, a + b
    if a % 2 == 0:
        sum += a
print(sum)

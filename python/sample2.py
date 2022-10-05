x = int(input('Enter x: '))
if x > 100:
    k = x * 2
    if x >= 200:
        k = k * 3
    elif k < 300:
        k = k * 4
    else:
        k = k * 5
else:
    k = x * 3
print (k)
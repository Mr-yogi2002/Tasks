# pyramid number pattern
n = 20
for i in range(n):
    for j in range(n + i - 1):
        print('', end='')
    for k in range(1 * i + 1):
        print(k + 1, end='')
    print()
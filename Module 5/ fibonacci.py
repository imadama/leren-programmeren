def fibonacci(n):
    a, b = 0, 1
    resultaat = []
    for i in range(n):
        resultaat.append(a)
        a, b = b, a + b
    return resultaat

print(fibonacci(10))
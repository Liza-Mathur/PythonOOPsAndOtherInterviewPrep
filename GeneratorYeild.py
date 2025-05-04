def fibonaci():
    a = 0
    b = 1
    while True:
        c = a+b
        yield c
        a = b
        b = c

fib = fibonaci()
for k in range(20):
    print(next(fib))
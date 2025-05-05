def filterEven(numbers):
    for k in numbers:
        if k%2 == 0:
            yield k
        
def squareNumbers(numbers):
    for n in numbers:
        yield n**2

def pipeline(numbers):
    filtered = filterEven(numbers)
    yield from squareNumbers(filtered)


num = range(1,20)
for k in pipeline(num):
    print(k)
from functools import reduce

# 1st one
def squares(k):
    return k*k

num = range(1,10)
nums = map(squares, num)
for k in nums:
    print(k, end=' ')

print()

#2nd one
def checkPrime(k):
    if k < 2:
        return False
    for i in range(2,k):
        if k%i == 0:
            return False
    return True

num2 = range(1,100)
nums2 = filter(checkPrime, num2)
print(list(nums2))

# 3rd one
num3 = range(1,6)
product = reduce(lambda x,y : x*y , num3)
print(product)

# 4th One
people = [
    {"name": "Alice", "age": 25},
    {"name": "Charlie", "age": 20},
    {"name": "Bob", "age": 30}
]

listAge = sorted(people, key = lambda k : k['age'])
print(listAge)

listName = sorted(people, key = lambda k : k['name'])
print(listName)

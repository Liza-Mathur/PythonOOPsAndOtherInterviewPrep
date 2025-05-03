import time

def argumentsInfinite(*args, **kwargs):
    for k in args:
        print(k)
    for k,v in kwargs.items():
        print("Key - ", k, " value - ", v)

def mutableDefaultArgumnetBug(fruit, l = []) -> list:
    l.append(fruit)
    return l

def mutableDefaultArgumnetBug_FIXED(fruit, l = None) -> list:
    if l is None:
        l=[]
    l.append(fruit)
    return l

def closureMultiplyNumbersByFixedNumbers(nList : list):
    def fixedNum(x):
        def variableNum(y):
            return x*y
        return variableNum

    multiply4 = fixedNum(4)
    for n in nList:
        print(multiply4(n))

def decoraterFuncion(func):
    def wrapper():
        print(time.time())
        print(time.perf_counter())
        func()
        print(time.time())
        print(time.perf_counter())
    return wrapper

@decoraterFuncion
def newFunc():
    for k in range(1,10000):
        pass


    
if __name__=="__main__":
    # 20 
    argumentsInfinite(1,2,3,4,5,6,7,8,[1,3,4,5,6], {1:'a', 2:'b', 3:'c'},{1:'a', 2:'b', 3:'c'})
    argumentsInfinite() #Won't give error. 

    # 21 
    mutableDefaultArgumnetBug("apple")
    mutableDefaultArgumnetBug("banana")
    print(mutableDefaultArgumnetBug("grapes"))
    # Must print apple, banana, grapes --> It did

    mutableDefaultArgumnetBug_FIXED("apple")
    mutableDefaultArgumnetBug_FIXED("banana")
    print(mutableDefaultArgumnetBug_FIXED("grapes"))
    # Must print grapes only --> It did

    # 22
    closureMultiplyNumbersByFixedNumbers([2,3,4,5,6,7,8,9,0])

    # 23
    newFunc()


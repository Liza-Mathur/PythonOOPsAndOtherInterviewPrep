names = ['liza', 'aline', 'sama']
age = [22, 34, 46]

def getNames():
    for k in names:
        yield k
    
def getAge():
    for k in age:
        yield k
    
def getSenteces():
    for n, a in zip(getNames(), getAge()):
        yield f"{n} is {a} years old"
    
if __name__=="__main__":
    for k in getSenteces():
        print(k)
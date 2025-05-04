class ObjectCunter():
    counter = 0

    def __init__(self):
        ObjectCunter.counter += 1
        print(ObjectCunter.counter)
    
o = ObjectCunter()
o2 = ObjectCunter()
o3 = ObjectCunter()
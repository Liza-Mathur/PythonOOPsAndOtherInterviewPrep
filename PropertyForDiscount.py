class Discount():
    def __init__(self, totalAmt):
        self.amount = totalAmt
    
    @property
    def discountedAmt(self):
        return self.amount * 0.05
    
d = Discount(5000)
print(d.discountedAmt)
d = Discount(100)
print(d.discountedAmt)
d = Discount(6888)
print(d.discountedAmt)
# here we dont call discountedAmt, its actually now a attribute. 
# Sort of a calculated attribute, which cannot be changed. Just be calculated
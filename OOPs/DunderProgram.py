class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self, other):
        return self.num+other.num
num1=int(input('Enter the first number:-  '))
num2=int(input('Enter the first number:-  '))
n1=Number(num1)
n2=Number(num2)    
print("addition of the two  number",n1+n2)

a=int(input('Enter the value of a ='))
b=int(input('Enter the value of b ='))
try:
    print(a/b)
except Exception as err :
       print(f'If try block will not execute i will run {err}')
finally:
        print('i will run everytime')
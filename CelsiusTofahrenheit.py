c=int(input('Enter the celsius value:- '))
far=(c * 9//5)+32
if far>=50:
  print(f'Farrenheit value is {far}F and moderate weather')
elif far<50 and far>=25:
   print(f'Farrenheit value is {far}F and cold weather')
elif far<24:
   print(f'Farrenheit value is {far}F and freezing weather') 
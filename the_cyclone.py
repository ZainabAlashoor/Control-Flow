'''Codédex: The Cyclone'''

height = int(input('Enter your height: '))
credit = int(input('Enter your credits: '))

if height>=137 and credit>=10:
  print('"Enjoy the ride!')
elif height>=137 and credit<10:
  print('You don\'t have enough credits.')
elif height<137 and credit>=10:
  print('You are not tall enough to ride.')
else:
  print('You can\'t ride, you haven\'t met either of the requirement')

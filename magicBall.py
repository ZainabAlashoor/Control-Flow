'''Codédex: Magic 8 Ball'''

import random

question = input('Enter any yes \ no question: ')

answer = random.randint(1,8)

if answer == 1:
  answer = 'Yes - definitely.'
elif answer == 2:
  answer = 'It is decidedly so.'
elif answer == 3:
  answer = 'Without a doubt.'
elif answer == 4:
  answer = 'Reply hazy, try again.'
elif answer == 5:
  answer = 'Ask again later.'
elif answer == 6:
  answer = 'Better not tell you now.'
elif answer == 7:
  answer = 'My sources say no.'
elif answer == 8:
  answer = 'Very doubtful.'

print('magic ball processing ~~')
print('-----------------------------')
print('Question: ', question)
print('Magic 8 Ball: ', answer)
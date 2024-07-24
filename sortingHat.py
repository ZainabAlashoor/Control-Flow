'''Codédex: sorting Hat'''

print ('Are you curious to know which of the great 4 houses you belong to?')
print('Here\'s a simple test to help you!')
print('You only have to answer a few quenstions~')

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Q1) Do you like Dawn or Dusk?')
print('    1) Dawn')  
print('    2) Dusk') 

q1 = int(input('Your answer: '))  

if q1 == 1:
  Gryffindor +=1
  Ravenclaw +=1
elif q1 == 2:
  Hufflepuff +=1
  Slytherin +=1
else: 
  print('wrong answer')

print('Q2) When I\'m dead, I want people to remember me as:')
print('    1) The Good')
print('    2) The Great')  
print('    3) The Wise')  
print('    4) The Bold')

q2 = int(input('Your answer: '))  

if q2 ==1:
  Hufflepuff +=2
elif q2 ==2:
  Slytherin +=2
elif q2 ==3:
  Ravenclaw +=2
elif q2 ==4:
  Gryffindor +=2
else: 
  print('wrong answer')

print('Q3) Which kind of instrument most pleases your ear?')
print('    1) The violin')    
print('    2) The trumpet')   
print('    3) The piano')   
print('    4) The drum')  

q3 = int(input('Your answer: '))  

if q3 ==1:
  Slytherin +=4
elif q3 ==2:
  Hufflepuff +=4
elif q3 ==3:
  Ravenclaw +=4
elif q3 ==4:
  Gryffindor +=4
else: 
  print('wrong answer')

print('---------------------------------')

if Gryffindor>Slytherin and Gryffindor>Ravenclaw and Gryffindor>Hufflepuff:
  print('Your house is 🦁 Gryffindor')
elif Ravenclaw>Gryffindor and Ravenclaw>Slytherin and Ravenclaw>Hufflepuff:
  print('Your house is 🦅 Ravenclaw')
elif Hufflepuff>Gryffindor and Hufflepuff>Slytherin and Hufflepuff>Ravenclaw:
  print('Your house is 🦡 Hufflepuff')
else:
  print('Your house is 🐍 Slytherin')

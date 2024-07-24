'''Codédex: pH Levels'''

print('check whether a pH level is basic, acidic, or neutral.')
ph = int(input("Enter a pH between (0-14): "))

if ph >7:
  print('Basic')
elif ph<7:
  print('Acidic')
else: 
  print('Neutral')

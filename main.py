import random

All_letter = ['first','maple','third']

Selected_word = list(random.choice(All_letter))


life = 5


WordLength = 5
blankleft = 5


display = []

Number_of_blank_left = WordLength

for _ in range(WordLength):
  display += "_"
print(display)





### check word match
def CheckWord():
  for i in range(len(Selected_word)):
    ### check if player input is same letter as selected word letter
    if player_input == Selected_word[i]:
      display[i] = Selected_word[i]
  
      print(display)
  CheckReduceLife() 
  
  


def CheckReduceLife():
  global blankleft
  global life
  global Number_of_blank_left
  blankleft = 0
  ###loop check blank left###
  for j in range(len(display)):
    if display[j] == '_':
      blankleft += 1


  print('There are {f} blank left'.format(f = blankleft))
  ### if blank left is equal to default blank left remove life
  if blankleft == Number_of_blank_left:
    life -= 1
    print('you have{f} live left'.format(f = life))
  elif blankleft < Number_of_blank_left: ### if blank left is not equal to blank left dont remove life
    print('you have selected correct word')
    Number_of_blank_left = blankleft
    
    
  




while True:


  if life > 0 and blankleft > 0:
    player_input = input('Enter letter: ').lower()
    CheckWord()
  elif life == 0:
    print('You lost')
    break
  elif blankleft == 0:
    print('You Won')
    break
  






    



    ### display blank word position






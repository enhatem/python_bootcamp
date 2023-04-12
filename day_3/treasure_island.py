print('''
     "Mystery is the key to enchantment"             
              ,d@@b,                    \.             
     ._.__._._@@@@@@__...__.._..___._. _) `----._ ._..__._._.__.___._._
             -_-__-_-               _.'         e`.__
              -_-__-           _ ,-'..---~~~)/---'~~~
                _-       _ - '.,',',-       '
                          -  -_ -_ -
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

ans_1 = input("You are at an intersection, which direction will you choose ? Left or Right ? ")
if ans_1.lower() == 'left':
  ans_2 = input("You reached a river. What will you do? Swim or Wait ? ")
  if ans_2.lower() == 'wait':
    ans_3 = input("You waited for a boat and arrived safely to the other side.\nThere are 3 colored doors ahead. Which colored door will you choose? Red, Yellow or Blue? ")
    if ans_3.lower() == 'yellow':
      print("You arrived to Subway. You win!")
    elif ans_3.lower() == 'red':
      print("The floor is lava. Game over.")
    elif ans_3.lower() == 'blue':
      print('You open the door and get eaten by a lion. Game over.')
    else:
      print('you decided to go back home. Game over.')
  else:
    print("You got hit by a dolphin. Game over.")
else:
  print("You got hit by a bus. Game over.")
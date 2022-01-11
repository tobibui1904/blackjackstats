import random
from random import randrange
import sys
import string
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#cards used in a standard blackjack game
blackjack=[1,2,3,4,5,6,7,8,9,10,'J','Q','K','A']

#draw cards to player and housebet
def drawcard(player):
  player=[]
  pos=random.randint(0,len(blackjack)-1)
  letter=blackjack[pos]
  pos1=random.randint(0,len(blackjack)-1)
  num=blackjack[pos1]
  player=[letter,num]
  return player

# list containing 2 list elements' points: players, housebet
player_list=[]

# list containing player's money after each turn
money_list=[]

# player's iniial money and bet
player_money=float(input('How much money do you have? (Minimum is $100.000) '))
while player_money < 100000:
    player_money=float(input('Please retype the money you have? (Minimum is $100.000) '))

player_bet=float(input('What is your bet? (Minimum is $1000) '))
while player_bet > player_money or player_bet < 1000:
  player_bet=float(input('Please retype the money you want to bet? (Minimum is $1000) '))

# Counting turns of play
turn=0

# enter procedure to store the player's money after each turn
def enter():
    enter=input('Please click enter to update your money: ')
    while enter not in (''):
      enter=input("Don't forget to click enter:")
    
#play the game
def play(player,whose_turn):
  global turn
  global player_money
  signal='Blackjack'
  point=0
  player=drawcard(player)
  print(whose_turn)
  print(player)
  # situation 1: first card is a integer
  if type(player[0])==int:
    if player[1]=='J' or player[1]=='Q' or player[1]=='K':
      print(player[0]+10)
      point=player[0]+10
    if player[1]=='A':
      if player[0]+11==21:
        print(signal)
        print(11)
        point=21
        
      else:
        print(player[0]+11)
        print(player[0]+1)
        point=player[0]+11

  # situation 2: first card is either J or Q or K
  if player[0]=='J' or player[0]=='Q' or player[0]=='K':
    if player[1]=='J' or player[1]=='Q' or player[1]=='K':
      print(20)
      point=20

    elif player[1]=='A':
      print(signal)
      print(11)
      point=21
      
    else:   
      print(10+player[1])
      point=10+player[1]

  #situation 3: first card is an A
  if player[0]=='A':
    if player[1]=='J' or player[1]=='Q' or player[1]=='K' or player[1]==10:
      print(signal)
      print(11)
      point=21
   
    elif player[1]=='A':
      print(22)
      print(2)
      point=2

    elif type(player[1])==int:
      sum=11+player[1]
      if sum==21:
        print(signal)
        point=21

      else:
        print(sum)
        point=11+player[1]
      print(1+player[1])

  # situation 4: both cards are integers
  if type(player[0])==int and type(player[1])==int:
    print(player[0]+player[1])
    point=player[0]+player[1]

  # blackjack signal system
  done = False
  while not done:
    print()
    next_draw = input("Hit card or Stand or Double Down or Surrender or analyst (to analyse your stats after playing the game) or shut down (to exit the game whenever you want): ").strip(string.punctuation).lower()

    # The hit signal
    if next_draw=='hit':
      point=0
      j = randrange(len(blackjack))
      item = blackjack[j]
      player.append(item)
      print(player)
      
      # calculate the sum of integer element in the list
      n=[]
      for item in player:
        if isinstance(item,int):
          n.append(item)
          total = 0
          for ele in range(0, len(n)):
            total = total + n[ele]

      # define the sum rules of strings and caclculate sum of the entire list
      countJ=player.count('J')
      countQ=player.count('Q')
      countK=player.count('K')
      countA=player.count('A')
      a=10*countJ
      c=10*countQ
      d=10*countK
      e=1*countA
      f=11*countA 
      sum_int=total
      sum_no_A=a+sum_int+c+d
      sum_A_11=a+sum_int+c+d+f
      sum_A_1=a+sum_int+c+d+e
      
      if 'A' not in player:
        if sum_no_A==21:
          print(signal)
          player_money=player_money+player_bet*1.5
          print('Now you have',player_money)
          print()
          point=sum_no_A
          done=True

        elif sum_no_A<21:
          print(sum_no_A)
          point=sum_no_A

        else:
          print(sum_no_A,'is larger than 21','so you lose')
          player_money=player_money-player_bet
          print('Now you have',player_money)
          turn+=1
          print('This is the', turn,'turn')
          print()
          point=0
          done=True

      elif 'A' in player:
        if sum_A_11==21:
          print(signal)
          player_money=player_money-player_bet
          print('Now you have',player_money)
          print()
          point=21
          done=True

        elif sum_A_11>21:
          pass

        else:
          print(sum_A_11)
          point=sum_A_11

        if sum_A_1==21:
          print(signal)
          player_money=player_money+player_bet*1.5
          print('Now you have',player_money)
          print()
          point=21
          done=True

        elif sum_A_1<21:
          print(sum_A_1)
          point=sum_A_1

        else:
          print(sum_A_1,'is larger than 21','so you lose')
          player_money=player_money-player_bet
          print('Now you have',player_money)
          turn+=1
          print('This is the', turn,'turn')
          print()
          point=0
          done=True

        if sum_A_11>21:
          point=sum_A_1

        else:
          point=sum_A_11

      if len(player)==5:
        if sum_no_A==21 and 'A' not in player:
          print(signal)
          player_money=player_money+player_bet*1.5
          print('Now you have',player_money)
          print()
          point=21
          done=True

        elif sum_no_A<21 and 'A' in player:
          print('win')
          player_money=player_money+player_bet*1.5
          print('Now you have',player_money)
          print()
          point=21
          done=True

        else:
          print(sum_A_1,'is larger than 21','so you lose')
          player_money=player_money-player_bet
          print('Now you have',player_money)
          turn+=1
          print('This is the', turn,'turn')
          print()
          point=0
          done= True

    # the double down signal
    elif next_draw=='double down':
        q = randrange(len(blackjack))
        item1 = blackjack[q]
        player.append(item1)
        print(player)
        n=[]
        countJ=player.count('J')
        countQ=player.count('Q')
        countK=player.count('K')
        countA=player.count('A')
        a=10*countJ
        c=10*countQ
        d=10*countK
        e=1*countA
        f=11*countA
        for item1 in player:
          if isinstance(item1,int):
            n.append(item1)
            total = 0
          for ele in range(0, len(n)):
            total = total + n[ele]
       
        sum_int=total
        sum_no_A=a+sum_int+c+d
        sum_A_11=a+sum_int+c+d+f
        sum_A_1=a+sum_int+c+d+e

        if 'A' not in player:
          if sum_no_A>21:
            print('You lost')
            print(sum_A_1,'is larger than 21','so you lose')
            player_money=player_money-player_bet
            print('Now you have',player_money)
            turn+=1
            print('This is the', turn,'turn')
            print()
            point=0
            done=True

          else:
              print(sum_no_A)
              point=sum_no_A
        elif 'A' in player:
          if sum_A_11>21:
            pass
          elif sum_A_11<21:
            print(sum_A_11)
            point=sum_A_11  
          else:
            print(sum_A_1)
            point=sum_A_1
            done=True
          if sum_A_11>21:
            point=sum_A_1
          else:
            point=sum_A_11
        player_list.append(point)
        for i in range(len(player_list)):
          if i==0:
            pass
          else:
            if player_list[0]>player_list[1]:
              print('Player win')
              player_money=player_money+player_bet*2
              print('Now you have',player_money+player_bet*2)
              print()
            
            elif player_list[0]==player_list[1]:
              print('Tie game')
            else:
              print('The house win')
              player_money=player_money-player_bet*2
              print('Now you have',player_money)
              print()
        done=True

    # the surender signal
    elif next_draw=='surrender':
      player_money=player_money
      print('Now you have',player_money)
      print()
      done=True
    
    elif next_draw=='shut down':
      sys.exit(-1)
      
    # the stand signal
    elif next_draw == "stand":
      y=money_list
      x=player_list
      x.append(point)
      for i in range(len(x)):
          if i==0:
            pass
          elif i==1:
            if x[0]>x[1]:
              print('Player win')
              player_money=player_money+player_bet
              print('Now you have',player_money)
              turn+=1
              print('This is the', turn,'turn')
              enter()
              y.append(player_money)
              print()

            elif x[0]==x[1]:
              print('Tie game')
              player_money=player_money
              print('Now you have',player_money)
              turn+=1
              print('This is the', turn,'turn')
              enter()
              y.append(player_money)
              print()

            else:
              print('The house win')
              player_money=player_money-player_bet
              print('Now you have',player_money)
              turn+=1
              print('This is the', turn,'turn')
              enter()
              y.append(player_money)
              print()
            x.clear()
      done = True

    elif next_draw=='analyst':
      print("turn", '\t', "money you have after each turn")
      print("---", '\t', "-----")
      y=money_list
      i=1
      for j in y[:]: 
          print(i, '\t', j)
          i+=1
      print('After',turn,'turn',"here's your statistic")
      print()
      total=0
      for ele in range(0, len(y)):
        total = total + y[ele]
      print('On average','you earn',"$",total/len(y))
      print('the maximum amount you earn is',"$",max(y))
      print('the minimum amount you earn is',"$",min(y))

      # Machine learning function: used to predict trends of player's money
      x = np.array(y)
      condlist = [x<10000000000000]
      choicelist = [x]
      xpoints = np.arange(1,turn+1)
      ypoints = np.select(condlist,choicelist)
      
      slope, intercept, r, p, std_err = stats.linregress(xpoints, ypoints)
  
      # function that is used to predict the money player is likely to earn after whatever turns he wants the graph to predict in the future
      def myfunc(xpoints):
        return slope * xpoints + intercept
      mymodel = list(map(myfunc, xpoints))

      plt.scatter(xpoints, ypoints,marker = '*')
      plt.plot(xpoints, mymodel)
      plt.xlabel("Turn")
      plt.ylabel("Money")
      plt.title("Linear regression of player'money ")

      prediction=int(input('Turns you want to predict '))
      while prediction< turn:
        prediction= int(input("Make sure it's the turn in the future! "))
      print("In the future, you might have",myfunc(prediction),"in turn",prediction)
      plt.show()
      
      sys.exit(-1)

# play the game function
def run():
  while True:
    player_turn="player's turn"
    housebet_turn="housebet's turn"
    player=[1,1]
    housebet=[1,1]
    play(drawcard(player),player_turn)
    play(drawcard(housebet),housebet_turn)

# main function
def main():
  print('Enter this code to join the game: (blackjack.txt) ')
  file_name = input("Enter your file name: ").strip(string.punctuation).lower()
  print()
  while file_name not in('blackjack.txt'):
    file_name=input('Try again ')
  my_file = open(file_name, "r")
  print(my_file.read())
  print()
  ans=input('Do you know the rules (y/n) ').strip(string.punctuation).lower()
  while ans not in('y','n'):
    ans=input('Try again ')
  if ans=='y':
      run()
  elif ans=='n':
    rule_name = 'rule.txt'
    my_rule = open(rule_name, "r")
    print(my_rule.read())
    print()
    run()
main()











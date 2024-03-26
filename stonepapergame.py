import random
while(True):

     comp = random.randint(0,2)
     print('0=stone','1=paper','2=scissor')
     user = int(input("enter your number"))
     print('the choice of computer is',comp)
     print('the choice of user is',user)
     if (comp==0 and user==0 ):
         print('tie')
     elif(comp==0 and user==1):
         print('user win')
     elif(comp==0 and user==2):
         print('comp wins')
     elif(comp==1 and user==0):
         print('comp wins')
     elif(comp==1 and user==1):
         print('tie')
     elif(comp==1 and user==2):
         print('user wins')
     elif(comp==2 and user==0):
         print('user wins')
     elif(comp==2 and user==1):
         print('comp win')
     elif(comp==2 and comp==2):
         print('Tie')
     else:
         print('wrong inp')


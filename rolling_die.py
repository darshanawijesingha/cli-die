#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
#play the die in once
roll =lambda :random.randint(1,6)
#define the rounds

def dies(rounds):
    player1=input("ENTHER THE 1ST PLAYER NAME ")
    player2=input("ENTHER THE 2ND PLAYER NAME ")
    mark1=0
    mark2=0
    term=1
    while term<=rounds:
        p1=roll()
        p2=roll()
        
        print("{} roll: {} | {} roll: {}".format(player1,p1,player2,p2))
        
        if p1==p2:
            print("draw")
        elif p1>p2:
            print("wow {}".format(player1))
            mark1+=1
        else:
            print("wow {}".format(player2))
            mark2+=1
            
        term+=1
        print("********************************************************")
    print("***************over******************************")
    if mark1==mark2:
        print("draw")
    elif mark1>mark2:
         print("wow {}".format(player1))
    else:
        print("wow {}".format(player2))
         


# In[4]:


dies(4)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





numoftries=0 
while numoftries !=3:
      username = input('insert your username: ')
      password= input('insert your password: ')
      if  username == 'drogba33' and password == 'drogbafilipo33': 
        print ('welcome shbiii')
        numoftries=0
        exit()
      else : 
         print('ser dber 3la rsk')
         numoftries+=1
         print('you have'+ str(3-numoftries)+ ' left :')
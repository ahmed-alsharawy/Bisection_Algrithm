print("think number between 0 and 100")
low=0
high=100
meduim=(low+high)//2
state=True
while state:
    print ("is your secret number =" + str(meduim))
    print("indicate your guess (h) if secret number is high ")
    print("indicate your guess (l) if secret number is low ")
    print("indicate your guess (c) if secret number is correct ")
    guess=input(" guess of your secret number is :  ")
    if  guess=='c':
        print ("game over , secret number is "+ str(meduim))
        state=False
    elif guess=='h':
        low=meduim;
        meduim=(high+low)//2
    elif guess=='l':
        high=meduim
        meduim=(high+low)//2
    else:
        print(" sorry ,I don't understand your gess")

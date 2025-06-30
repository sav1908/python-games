#create a number using randint bw 1 - 100 then give 3 chances to guess the number, give hints during guess
from random import randint
hid = randint(1,100)

for i in range(3):
    c1 = int(input("Guess the number from 1 to 100 "))
    if c1 == hid:
        print("You win")
        break
    elif c1 < hid:
        print("Number is higher than", c1,'guess again ')
    elif c1 > hid:
        print("Number is lower than", c1,'guess again ')
else:
    print("You lose, the number is", hid)

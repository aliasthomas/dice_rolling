import random

# randint function to generate the
# random number b/w 1 to 6

name = input("Enter your name: ")
print("Hi,{} welcome to dice rolling".format(name))
print("The rolling only stop until you give 'n' as input")

s = input("To roll  input y/n: ") #The is given here

while s.lower() =='y':

        #while loop check the input with lower case

        a = random.randint(1,6)# assign random numbers
        b = random.randint(1,6)
        print(a)
        print(b)
        s = input("To roll  input y/n: ")# To roll again input is given here
        if s.lower() == 'n':

            # Compare the user entered input

            print("Thanks for rolling")
        else:
            print("invalid input") #Used to give alert on other than y/n

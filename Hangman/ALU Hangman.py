# Name
print("Name: Mahalinoro Razafimanjato" + "\n")

#This is for the function sys to exit the code basically
import sys
# The ALU Hangman is a program that asks a series of question to the user, if they got the right asnwers they don't hang the man
# But in the contrary, they will hang the man and if they keep having wrong answers, the man will die then the game ends

print("Welcome to ALU Hangman!!")
print("Let's get started:" + "\n")

#This function ask 10 questions for the users
#The way it is done in order for the game to stop or not, there is the score system

def ask_questions():
#The score at the beginning will be score = 0 then after answering the proper answer 1 point will be assigned unless 0 for the wrong answer
    score = 0
    #First question
    first_question = int(input("1. When was ALU founded? (year): "))
    if first_question == 2015:
        score +=1
        print("Yes, you are right!!")
    else:
        score -=0
        print("Oh! Wrong answer... You hanged your man!")
    #Second question
    second_question = str.lower(input("2. Who is the CEO of ALU?: ")) #So whatever input the user will insert, the program will convert it into lowercase
    if second_question == "fred swaniker" : #So it will handle answer properly
        score +=1
        print("Are you a genius? Because you are right!")
    else:
        score -=0
        print("Oh! Wrong answer... You hanged your man!")
    #Third question
    third_question = str.lower(input("3. Where are the ALU campuses?: "))
    if third_question == "rwanda and mauritius" or third_question == "mauritius and rwanda":
        score +=1
        print("You are right!")
    else:
        score -=0
        print("Oh! Wrong answer... You hanged your man!")
    #Fourth question
    fourth_question = str.lower(input("4. What is the name of the ALU Rwanda's Dean?: "))
    if fourth_question == "gaidi faraj":
        score +=1
        print("Super! You are right!")
    else:
        score -=0
        print("Oh! Wrong asnwer... You hanged your man!")
    #Filth question
    filth_question = str.lower(input("5. Who is in charge of Student Life?: "))
    if filth_question == "sila ogidi":
        score +=1
        print("Very good! It's true.")
    else:
        score -=0
        print("Oh! Wrong answer... You hanged your man!")
    #Sixth question
    sixth_question = str.lower(input("6. What is the name of our lab?: "))
    if sixth_question == "nigeria":
        score +=1
        print("Good answer!")
    else:
        if score == 0:
            sys.exit("Sorry, but your man dies! You can do better next time!") #Here, the program will stop if the user get wrong 6 times
        else:
            print("Oh! Wrong answer... You hanged your man!")
    #Seventh question
    seventh_question = int(input("7. How many students do we have in year 2 CS?: "))
    if seventh_question == 57:
        score +=1
        print("Correct! Snaps for you!")
    else:
        if score <= 1: #for this, the game will stop as well
            sys.exit("Sorry, but your man dies! You can do better next time!")
        else:
            print("Oh! Wrong answer... You hanged your man!")
    #Eighth question
    eighth_question = int(input("8. How many degrees does ALU offer?: "))
    if eighth_question == 8:
        score +=1
        print("Correct!!")
    else:
        if score <= 2: #The same as the above
            sys.exit("Sorry, but your man dies! You can do better next time!")
        else:
            print("Oh! Wrong answer... You hanged your man!")
    #Nineth question
    nineth_question = int(input("9. How many campuses does ALU Have?: "))
    if nineth_question == 2:
        score +=1
        print("Good! You are right!")
    else:
        if score <= 3:
            sys.exit("Sorry, but your man dies! You can do better next time!")
        else:
            print("Oh! Wrong answer... You hanged your man!")
    #Tenth question
    tenth_question = str.lower(input("10. Where are the headquarters of ALU?: "))
    if tenth_question == "mauritius": #This one ine particular is for the last question if the user reach the last one
        score +=1
    else:
        if score <= 4:
            sys.exit("Sorry, but your man dies! You can do better next time!")
    mistake = 9 - score
    print("You score is " + str(score) + " and you have made " + str(mistake) + " mistakes.")
    sys.exit("Congratulations, you have gone through it!!")

ask_questions()


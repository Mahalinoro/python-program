# Name
print("Mahalinoro Razafimanjato" + "\n")

# This program is the upgraded version of Hangman with the option of starting the game again
print("Welcome to Hangman!")
print("You will be prompted to answer 10 questions. Good Luck! Try not to hang your man!")
print("Let's get started: " + "\n")

# They will help us keep track of the losses and wins
# They will become global variables when assigned into the functions because we want to keep the values intact
loss = 0
win = 0

def main():
    # This function will ask 10 questions to the user
    # Every time they get the right answer, it will add 1 point to the initial score
    # If it is not the case, then it doesn't attribute the point but the man is starting to be hanged
    # It will display the number of losses and wins
    # It will count and calculate mistakes and right answers
    # Variables to start with, they will help us keep track of the user's progress
    global win
    global loss
    score = 0
    # first question
    first_question = int(input("1. When was ALU founded? (yyyy): "))
    if first_question == 2015:
        score += 1
        print("Good answer!")
    else:
        score -= 0
        print("Wrong answer! You just started to hang your man.")
    # second question
    second_question = str.lower(input("2. Who is the CEO Of ALU?: "))
    if second_question == "fred swaniker":
        score += 1
        print("You got it right!")
    else:
        score -= 0
        print("Wrong answer! Your man is in danger... Be careful!")
    # third question
    third_question = str.lower(input("3. Where are the ALU campuses? (x and y) : "))
    if third_question == "rwanda and mauritius" or third_question == "mauritius and rwanda":
        score += 1
        print("Very good!")
    else:
        score -= 0
        print("Wrong answer! You can do better...")
    # Fourth question
    fourth_question = str.lower(input("4. What is the name of ALU Rwanda's dean?: "))
    if fourth_question == "gaidi faraj":
        score += 1
        print("Are you a genius? You're right!")
    else:
        score -= 0
        print("Wrong answer!")
    # Filth question
    filth_question = str.lower(input("5. Who is in charge of Student Life?: "))
    if filth_question == "sila ogidi":
        score += 1
        print("Very good! It's true.")
    else:
        score -= 0
        print("Oh! Wrong answer...")
    # Sixth question
    sixth_question = str.lower(input("6. What is the name of our lab?: "))
    if sixth_question == "nigeria":
        score += 1
        print("Good answer!")
    else:
        if score == 0:
            loss += 1
            print("Sorry, but your man dies!")
            restart = input("Do you wish to restart again? (yes, yeah, y/ no, n): ")
            if restart == "yes" or restart == "yeah" or restart == "y":  # This will ask if the user want to play again
                main()
            else:
                exit("You have made " + str(win) + " win(s) " + "and " + str(loss) + " loss(es).")
        else:
            print("You are wrong!")
    # Seventh question
    seventh_question = int(input("7. How many students do we have in year 2 CS?: "))
    if seventh_question == 57:
        score += 1
        print("Correct! Snaps for you!")
    else:
        if score <= 1:
            loss += 1
            print("Sorry, but your man dies! You can do better!")
            restart = input("Do you wish to restart again? (yes, yeah, y/ no, n): ")
            if restart == "yes" or restart == "yeah" or restart == "y":
                main()
            else:
                exit("You have made " + str(win) + " win(s) " + "and " + str(loss) + " loss(es).")
        else:
            print("Oh! Wrong answer...!")
    # Eighth question
    eighth_question = int(input("8. How many degrees does ALU offer?: "))
    if eighth_question == 8:
        score += 1
        print("Correct!!")
    else:
        if score <= 2:
            loss += 1
            print("Sorry, but your man dies!")
            restart = input("Do you wish to restart again? (yes, yeah, y/ no, n): ")
            if restart == "yes" or restart == "yeah" or restart == "y":
                main()
            else:
                exit("You have made " + str(win) + " win(s) " + "and " + str(loss) + " loss(es).")
        else:
            print("Oh! Wrong answer...!")
    # Ninth question
    ninth_question = int(input("9. How many campus does ALU have?: "))
    if ninth_question == 2:
        score += 1
        print("Correct! You are right!")
    else:
        if score <= 2:
            loss += 1
            print("Sorry, but your man dies!")
            restart = input("Do you wish to restart again? (yes, yeah, y/ no, n): ")
            if restart == "yes" or restart == "yeah" or restart == "y":
                main()
            else:
                exit("You have made " + str(win) + " win(s) " + "and " + str(loss) + " loss(es).")
        else:
            print("Oh! Wrong answer...!")
    # Tenth question
    tenth_question = str.lower(input("10. Where are the headquarters of ALU?: "))
    if tenth_question == "mauritius":
        score += 1
    else:
        if score <= 4:
            loss += 1
            print("Sorry, but your man dies! You can do better next time!")
            restart = input("Do you wish to restart again? (yes, yeah, y/ no, n): ")
            if restart == "yes" or restart == "yeah" or restart == "y":
                main()
            else:
                exit("You have made " + str(win) + " win(s) " + "and " + str(loss) + " loss(es).")
    print("Your man is alive! Congratulations!")
    mistake = 10 - score
    win += 1
    print("You score is " + str(score) + " and you have made " + str(mistake) + " mistakes.")
    restart = input("Do you wish to restart again? (yes, yeah, y/ no, n): ")
    if restart == "yes" or restart == "yeah" or restart == "y":
        main()
    else:
        exit("You have made " + str(win) + " win(s) " + " and " + str(loss) + " loss(es).")

main()

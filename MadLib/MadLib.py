#Name
print("Name: Mahalinoro Razafimanjato" + "\n")

#MadLib is a program that asks user to input words/verbs/expression in a specific story
#The users can have fun just by changing the expressions into new ones and create a funny story

print("Welcome to MadLib!!")
print("The powerful tool to modify any story and make it your own!" + "\n")

#The original story
def original_story():
    print("Title: The Story of Nehemiah and Paul" + "\n")
    print("King Nehemiah and Paul were childhood friends. While Nehemiah thrived and prospered, Paul didn’t.")
    print("He leads the life of a poor villager man, living in a small hut with his wife and kids.")
    print("Most days, the kids wouldn’t even get enough to eat from what Paul got as alms.")
    print("One day, his wife suggested that he go and ask his friend Nehemiah for help.")
    print("Paul was reluctant to seek favors, but he also didn’t want his kids to suffer.")
    print("So his wife borrows some rice from the neighbors to make some rice snacks that Nehemiah liked and gave it to Paul to take it to his friend.")
    print("Paul took it and headed to the kingdom. He was amazed at the gold that was used to build the city.")
    print("He reached the palace gates and was obstructed by the guards, who judged him by his torn robe and poor appearance.")
    print("Paul requested the guards to at least inform Nehemiah that his friend Paul has come to meet him.")
    print("The guard, although reluctant, goes and informs the lord. On hearing that Paul was here, Nehemiah stops doing whatever he was doing and runs barefoot to meet his childhood friend.")
    print("Nehemiah hugs Paul welcomes him to his abode and treats him with utmost love and respect.")
    print("Paul, ashamed of the poor man’s rice snacks he got for Nehemiah, tries to hide it.")
    print("But the all-knowing Nehemiah asks him for his gift and eats his favorite rice snacks that his friend brought for him.")
    print("Nehemiah and his friend spend time laughing and talking about their childhood but Paul, overwhelmed by the kindness and compassion showed by his friend, is unable to ask Nehemiah for help.")
    print("When he returns home, Paul finds that his hut has been replaced by a huge mansion and his wife and kids are dressed in fine clothes.")
    print("He realized how lucky he was to have a true friend like the King. He didn’t even ask, but Nehemiah knew what Paul wanted and gave it to him.")

print("This is the original story")
#Calling the function for the original story
original_story()

print("\n" + "Now, you have the power to change the story")
print("Let's begin, shall we?!")

#The modified story
def modified_story():
#Code for the questions
    name_character_1 = input("Insert a new name for Nehemiah: ")
    name_character_2 = input("Insert a new name for Paul: ")
    verb_past_1 = input("Insert a verb in past tense: ")
    verb_past_2 = input("Insert another verb in past tense: ")
    adj_1 = input("Insert an adjective(poor/rich/average): ")
    noun_1 = input("Insert a noun(villager/citizen/noble...): ")
    adj_2 = input("Insert an adjective(small, big, ...): ")
    noun_2 = input("Insert a noun(place to live, house, mansion...): ")
    verb_present = input("Insert a verb in present tense: ")
    noun_3 = input("Insert a noun (food related): ")
    noun_4 = input("Insert a noun (place/castle/mansion...): ")
    adj_3 = input("Insert an adjective for mood: ")
    adj_4 = input("Insert an adjective: ")
    verb_inf = input("Insert a verb in the infinitive without -to: ")
    verb_ing1 = input("Insert a verb in -ing form: ")
    verb_ing2 = input("Insert another verb in -ing form: ")
    adj_5 = input("Insert an adjective: ")
#Code for the output
    print("Title: The Story of " + name_character_1 +  " and " + name_character_2 + "\n")
    print("King " + name_character_1 + " and " + name_character_2 + " were childhood friends. While "+ name_character_1 + " " + verb_past_1 + " and, " + verb_past_2 + " " + name_character_2 +  " didn’t.")
    print("He leads the life of a " + adj_1 + " " + noun_1 + " man, living in a " +  adj_2 + " " + noun_2 + " with his wife and kids.")
    print("Most days, the kids wouldn’t even get enough to eat from what " + name_character_2 +" got as alms.")
    print("One day, his wife suggested that he go and ask his friend" + name_character_1 + " for help.")
    print(name_character_2 + " was reluctant to seek favors, but he also didn’t want his kids to suffer.")
    print("So his wife " + verb_present + " some " + noun_3 + " from the neighbors to make some " + noun_3 +" snacks that " + name_character_1 + " liked and gave it to " + name_character_2 + " to take it to his friend.")
    print(name_character_2 + " took it and headed to the " + noun_4 + ". He was " + adj_3 + " at the gold that was used to build the city.")
    print("He reached the palace gates and was obstructed by the guards, who judged him by his " + adj_4 + " robe and " + adj_1 + " appearance.")
    print(name_character_2 + " requested the guards to at least inform " + name_character_1 + " that his friend " + name_character_2 + " has come to meet him.")
    print("The guard, although reluctant, goes and informs the lord. On hearing that " + name_character_2 + " was here, " + name_character_1 + " stops doing whatever he was doing and runs barefoot to meet his childhood friend.")
    print(name_character_1 + " hugs " + name_character_2 + " welcomes him to his abode and treats him with utmost love and respect.")
    print(name_character_2 + "," + " ashamed of the poor man’s " + noun_3 + " snacks he got for "+ name_character_1 + ", tries to " + verb_inf +" it.")
    print("But the all-knowing, " + name_character_1 + " asks him for his gift and eats his favorite " + noun_3 + " snacks that his friend brought for him.")
    print(name_character_1 + " and his friend spend time " + verb_ing1 + " and " + verb_ing2 + " about their childhood but " + name_character_2 + ", overwhelmed by the kindness and compassion showed by his friend, is unable to ask " + name_character_1 + " for help.")
    print("When he returns home, "+ name_character_2 +" finds that his" + noun_2 + " has been replaced by a huge mansion and his wife and kids are dressed in fine clothes.")
    print("He realized how " + adj_5 + " he was to have a true friend like the King. He didn’t even ask, but " + name_character_1 + " knew what " + name_character_2 + " wanted and gave it to him.")

print("This is the modified story")
#Calling the function for the modified story
modified_story()


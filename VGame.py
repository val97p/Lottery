#introduction

name = input ("please, introduce your name ")


print (name + " welcome to The Lottery")

print (name + """, this is your last warning.
              
              You are in a place with no return""")

enter_question = input("do you take the risk? ")


if enter_question == "yes":
    print (name + " accepts the challenge")

elif enter_question == "no":
        print("Game over, Vaquero")


else:
    print ("Not Valid Command")
    while enter_question != "yes" or "no":
        enter_question = input("do you take the risk? ")
        if enter_question == "yes":
            print(name + " accepts the challenge")
            break

        elif enter_question == "no":
            print("Game over, Vaquero")
            break

x = "You got it"

y = (name + """ falls from  Necroshire Ravine.

                              You have to wait for someone to help

                              Game Over, """ + name)

z = "right, you are on the center"






if enter_question == "yes":
    print (name + """, you are in the Hells Gates/Paradide Falls/killmoor town. 

 Today is june 27, was clear and sunny, with the fresh warmth of a full-summer day; 
 the flowers were blossoming profusely and the grass was richly green ,a beautiful day for the town lottery. 
 
 In others towns, the Lottery takes longer, but there are only
  300  people in this village, so the lottery take only two hours.
  
    In Postville, The Lottery took two days. 
    
    now, you are in the Black Forest.
    
    You must go to Everwinter Lake to Pick up stones.
    """)
    question_move = input("Where do you go? ")

# move = north, south, west, east



    while question_move == 'north' or 'south' or 'east' or 'west':

        if question_move == 'north':
            print ("you are near Everwinter lake")
            question_action = input("What do you do? ")
            if question_action == "walk":
                print ("You find a bunch of stones")
                question_action = input("What do you do? ")
                if question_action == "pick up":
                    question_action1 = input ("what do you want to pick up? ")
                    if question_action1 == "stones":
                        print (x)

                        # second part

                        if x == "You got it":
                            print("Now, You have to go to The Center")
                            print("""" To arrive to the Center

                                                   you have to result the this Challenge 

                                                   There was a green house. Inside the green house there was a white house. 
                                                   Inside the white house there was a red house. Inside the red house there were lots of babies.""")

                            challenge_question = input(" What is it? ")

                            if challenge_question == "watermelon":
                                print("Right, you are almost there. You need to solve one more")
                                challenge_question2 = input(
                                    "What animal  walks on four legs in the morning, two legs at noon and three legs in the evening? ")

                                if challenge_question2 == "man":
                                    print(z)

                                    # Tird Part

                                    w = "people is gathering around The center"

                                    l = "Tessie Hutchinson arrived after everyone because she forgot the date"

                                    if z == "right, you are on the center":
                                        print(w)
                                        print(
                                            "Mr. Summers runs the lottery because he has a lot of time to do things for the village. "
                                            "He arrives in the square with the black box, followed by Mr. Graves, the postmaster. ")
                                        print("There is a sound form the back of the crowd")
                                        if w == "people is gathering around The center":
                                            question_action2 = input("what's next? ")
                                            if question_action2 == "look":
                                                print(l)

                                                if question_action2 == l:
                                                    print(
                                                        "Mr. summers'll read names, and the family heads come up and draw a slip of paper")
                                                    question_box = input("Who's got it? ")
                                                    if question_box == "me":
                                                        print(
                                                            "Mr. Summers asks whether there are any other households in the Salomon family. And you deny")
                                                        print(
                                                            "Mr. Summers calls your family names, each member of the family comes up and draws a paper")
                                                        print("Now, you have to open the paper")
                                                        question_paper = input("do " + name + " you gave a paper? ")
                                                        if question_paper == "yes":
                                                            print(
                                                                '"All right, folks." Mr. Summers said. "Finish quickly."')
                                                            print(name + "Salomon, you has to put on center")
                                                            print("Villagers grab stones and run toward you")

                                                        elif question_paper == "no":
                                                            print("Becky Salomon got it")
                                                            print(
                                                                '"All right, folks." Mr. Summers said. "Finish quickly."')
                                                            print("Becky Salomon, you has to put on center")
                                                            print("Villagers grab stones and run toward her")

                                                        else:
                                                            while question_paper != 'yes' or 'no':
                                                                question_paper = ("do " + name + " you gave a paper? ")
                                                                break
                                                else:
                                                    print("Bill Hutchinson's got it.")
                                                    print(
                                                        "Mr. Summers asks whether there are any other households in the Hutchinson family. And you deny")
                                                    print(
                                                        "Mr. Summers calls their names, each member of the family comes up and draws a paper")
                                                    print("Now, you have to open the paper")
                                            else:
                                                print("people joke about Tessie Hutchinson late arrival.")
                                                print(
                                                    "Mr. summers'll read names, and the family heads come up and draw a slip of paper")
                                                question_box = input("Who's got it? ")
                                                if question_box == "me":
                                                    print(
                                                        "Mr. Summers asks whether there are any other households in the Salomon family. And you deny")
                                                    print(
                                                        "Mr. Summers calls your family names, each member of the family comes up and draws a paper")
                                                    print("Now, you have to open the paper")
                                                    question_paper = input("do " + name + " you gave a paper? ")
                                                    if question_paper == "yes":
                                                        print(
                                                            '"All right, folks." Mr. Summers said. "Finish quickly."')
                                                        print(name + "Salomon, you has to put on center")
                                                        print("Villagers grab stones and run toward you")

                                                    elif question_paper == "no":
                                                        print("Becky Salomon got it")
                                                        print(
                                                            '"All right, folks." Mr. Summers said. "Finish quickly."')
                                                        print("Becky Salomon, you has to put on center")
                                                        print("Villagers grab stones and run toward her")

                                                    else:
                                                        while question_paper != 'yes' or 'no':
                                                            question_paper = ("do " + name + " you gave a paper? ")
                                                            break

                                        else:
                                            question_action2 = input("what's next? ")

                                else:
                                    while challenge_question2 != "man":
                                        print("Wrong answer, Try again")
                                        challenge_question2 = input(
                                            "What animal  walks on four legs in the morning, two legs at noon and three legs in the evening? ")
                                        break

                            else:
                                while challenge_question != "watermelon":
                                    challenge_question2 = input(" What is it? ")

                                    break

                    else:
                        while question_action1 != "stones":
                         print ("You cannot pick that")
                        question_action1 = input("what do you want to pick up? ")
                        break

                else:
                    while question_action != "pick up":
                        print ("Another action, please")
                        question_action = input("what do you do? ")
                    break


            else:
                while question_action == "walk":
                 print("Another action, please")
                 question_action = input("what do you do? ")
                 break

        if question_move == 'east':
            print ("you are near Necroshire Ravine")
            question_action = input ("What do you do? ")
            if question_action == 'walk':
                print (y)
                break

        elif question_move == 'south' or 'west':
            print ("You cannot go there")
            while question_move == 'south' or 'west':
                question_move = input("Where do you go? ")
                break

        else:
            print ("Not Valid Command")
            question_action = input("What do you do? ")
            break

x = "You got it"
y = (name + """ falls from  Necroshire Ravine.

                              You have to wait for someone to help

                              Game Over, """ + name)




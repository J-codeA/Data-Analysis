def main(): #Four parameters as inputs: Publisher, ESRB Rating, Platform, and Year
    Publisher = input("Who is your favorite publisher? "); #Publisher as in who issues games for sorted
    ESRB = input("What is the typical ESRB rating of the games you play? "); #ESRB Ratings shows intended audience for games
    Platform = input("What gaming system do you have? "); #Platform means what system the game can be played on
    Year = int(input("What year was your favorite game released? ")); #Year means what year the game was published

    if(Publisher == "EA Sports"): #If the Publisher is EA Sports
        if(ESRB == "E"): #And if the ESRB rating is E for Everyone
            print("You should buy a game in the Sports genre"); #User most likely likes a Sports game
        else:
            print("You should buy a game in the Fighting genre");
    else: #However if the publisher is not EA Sports, it moves on to other branches
        if(ESRB == "M"):  #Program goes through a list of the biggest game publishers if the rating is M for mature
            if(Publisher == "Midway Games"):
                print("You should buy a game in the Fighting genre");
            elif(Publisher == "Bethesda Softworks"):
                print("You should buy a game in the Role-Playing genre");
            elif(Publisher == "Electronic Arts" or Publisher == "Activision" or Publisher == "Sony Computer Entertainment"):
                print("You should buy a game in the Shooter genre");
            else:
                if(Year <= 1998): #This is one of the few times year is mentioned, indicating genree popularity specific to this period
                    print("You should buy a game in the Shooter genre");
                else:
                    if(Platform == "Xbox"): #Especially if the game was played on Xbox
                        print("You should buy a game in the Shooter genre");
                    else: #If not, then it was most likely an action game
                        print("You should buy a game in the Action genre");
        else:
            if(Publisher == "2k Sports"):
                print("You should buy a game in the Sports genre");
            else:
                if(ESRB == "E"): #If the ESRB rating is E for everyone 
                    if(Platform == "Nintendo DS"): #And if the platform is Nintendo DS
                        if(Publisher == "THQ"):
                            print("You should buy a game in the Adventure genre");
                        elif(Publisher == "Disney Interactive Studios"):
                            print("You should buy a game in the Action genre");
                        else: #Otherwise, it is a simulation gamee
                            print("You should buy a game in the Simulation genre");
                    else:  #Program goes through a list of the biggest game publishers 
                        if(Publisher == "Warner Bros. Interactive"):
                            print("You should buy a game in the Adventure genre");
                        elif(Publisher == "LucasArts"):
                            print("You should buy a game in the Action genre");
                        elif(Publisher == "Konami"):
                            print("You should buy a game in the Simulation genre");
                        elif(Publisher == "Namco"):
                            print("You don't have a specific genre.  You like various types of games");
                        elif(Publisher == "EA Sports BIG"):
                            print("You should buy a game in the Sports genre");
                        elif(Publisher == "Activision" or Publisher == "Sony Computer Entertainment"):
                            print("You should buy a game in the Platform genre");
                        elif(Publisher == "Sega"):
                            print("You should buy a game in the Sports genre");
                        else: #If the game was published by any of these, then the genre popularity was based on platform
                            if(Platform == "GBA"): #Especially if the game can be played by Nintendo
                                    print("You should buy a game in the Platform genre");
                            elif(Platform == "Wii"):
                                    print("You should buy a game in the Miscellaneous");
                            else:
                                print("You should buy a game in the Racing genre");
                else:
                    if(Platform == "PC"): #If the game is typically played on PC, it is most likely a simulation
                        print("You should buy a game in the Simulation genre");
                    else:
                        if(ESRB == "NA"):
                            if(Publisher == "Atari"):
                                print("You should buy a game in the Shooter genre");
                            else:
                                print("You should buy a game in the Action genre");
                        else:
                            if(Publisher == "MTV Games"):  #Program goes through a list of the biggest game publishers 
                                print("You don't have a specific genre.  You like various types of games");
                            elif(Publisher == "THQ" or Publisher == "Namco"):
                                print("You should buy a game in the Fighting genre");
                            elif(Publisher == "Eidos Interactive"):
                                print("You should buy a game in the Action genre");
                            elif(Publisher == "Activision"):
                                if(Year <= 2007): #One of the few times that a year was mentioned if the publisher is activision
                                    if(Year <= 2003): #If the game was made on or before 2003, it was a popular sports game
                                        print("You should buy a game in the Sports genre");
                                    else:
                                        if(Platform == "PS2"): #If it was made after 2003 but a PS2 game, most likely a Sports
                                            print("You should buy a game in the Sports genre");
                                        else: #Otherwise, user probably likes shooter genre games
                                            print("You should buy a game in the Shooter genre");
                                else:
                                    if(Year <= 2012): #Otherwise if it's not by Activision and published on or before 2012, it's more likely you don't have a specific favorite genre
                                        print("You don't have a specific genre.  You like various types of games");
                                    else: #Otherwise, user probably likes a shooter genre
                                        print("You should buy a game in the Shooter genre"); 
                            elif(Publisher == "Electronic Arts" or Publisher == "Ubisoft"):
                                print("You should buy a game in the Shooter genre");
                            elif(Publisher == "LucasArts"):
                                print("You should buy a game in the Action genre");
                            else:
                                if(Year < 2008): #If the game was published before 2008
                                    if(Publisher == "Sony Computer Entertainment"): #And by this publisher
                                        if(Platform == "PS2"): #And played on a PS2, it is most likely a platform genre
                                            print("You should buy a game in the Platform genre");
                                        else:
                                            print("You should buy a game in the Action genre");
                                    else:
                                        if(Year <= 2005): #If the game was published on or before 2005
                                            if(Platform == "PS2"):  #And played on a PS2, it is most likely a Racing genre
                                                print("You should buy a game in the Racing genre");
                                            else:
                                                print("You should buy a game in the Fighting genre");
                                        else: #If game wass published after 2005, user most likely likes various genress
                                            print("You don't have a specific genre.  You like various types of games");
                                else: #Otherwise, it is an action game
                                    print("You should buy a game in the Action genre");


main()
print("\n")
main()
print("\n")
main()

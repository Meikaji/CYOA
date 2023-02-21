name = input("Type your name: ")
print("Make sure to type each command shown in the parenthesis in ALL CAPS. Otherwise, the game will experience issues.")
print("You've awoken in a cave, surrounded by crates and the darkness. All that you have is a suit that seems to have been made for space travel and a helmet that has a large, visible crack on the visor. You hear the distant screeches of something. The horrific sound is rapidly approaching. You're unprepared to face this.")
print("There are three pathways, although all three are poorly lit. Pick one, or face the consequences. (LEFT/RIGHT/STRAIGHT)")

do = input(": ")
if do == "RIGHT":
        print("The path went on and on, curving in all sorts of directions. However, it seems that you managed to survive a fate that was coming for now. As you reach the end of the dark tunnel, you stop to catch a break.")
        print("You've arrived at a small room, that seemed to be fully furnished for some reason. your head starts to ring again as your memories seemed to dim. The path behind you is now gone entirely, and you stand right against the room's wall")
        print("Upon the table that sat at the center of the room was a plate of seemingly innocent cookies.")
        print("Your stomach rumbles as you're tempted to take one. It couldn't hurt to grab one, no? (RESIST/EAT)")

        do = input(":: ")
        if do == "EAT":
            print("You decide to cave and take one of these extremely tempting cookies.")
            print("The cookie almost instantly melts in your hand, the rest of your arm following as your body turns to an unrecoverable goop that spills from the cracks of the helmet.")
            print("You're Done. Cause: Contact with corrosive substances.")
            end = input("Type END to leave: ")

        elif do == "RESIST":
            print("ARE you sure you want to do this? You won't be able to go back if you leave this behind. (YES/GIVE IN)")

            do = input(":: ")
            if do == "YES":
                print("Shaking your head and coming back to your senses, you decide to go for the door, turning the handle.")
                print("The door opening seems to have opened up to a hallway, the lights flicker on and off, rapidly. just as you're about to step inside, a loud screech similar to the one in the cave can be heard behind you.")
                print("tH3 Th1nG 1s h3R3. (RUN/FACE THE CONSEQUENCES)")

                do = input(":: ")
                if do == "RUN":
                        print("You sprint across the hallway, not bothering to do so, and why would you? Running faster and faster, you can see a door and an open vent just below.")
                        print("Something tells you that you shouldn't but you think you can manage to fit into it. (BASH/VENT)")
                
                        do = input(":: ")
                        if do == "VENT":
                            print("You try to jump into the vent, but forget the fact that those are usually screwed down to the floor. Kinda a dumb move, which leaves you wide open for an attack")
                            print("Your neck was quickly snapped. How convinient")
                            print("You're done. Cause: Brain death.")
                            print("Deceased Identification:")
                            print(name)
                            end = input("Type END to leave: ")


                        elif do == "BASH":
                            print("It was quite logical to bash the door open rather than try to go into a vent. That would be very suspicious of you.")
                            print("The door completely breaks off the hinges due to your shoulders momentum, leading to a wide, dark room with a glowing red button in the middle.")
                            print("There's no other way to go. all that's left is the button and the massive window on the far wall, revealing the massive expanse of space, a seemingly unknown planet just in view.")
                            print("PRESS THE BUTTON/BASH")

                            do = input(":: ")
                            if do == "PRESS THE BUTTON":
                                print("You have no other choice, and proceed to slam your fist against the button.")
                                print("You shoot up from your bed, looking around. The familiar room that surrounds you makes you sigh in relief. It was just another nightmare.")
                                print("Let's hope you won't stay up all night because of it.")
                                print("GOOD END: Back to Reality")
                                print("Game made by:")
                                print("Diego Casillas")
                                print("Game play-tested by:")
                                print(name)
                                print("Thank you for playing my game :)")
                                end = input("Type END to leave: ")

                            elif do == "BASH":
                                print("You decide to take matters into your own hands, and run for the window. If you're going down, you're not going down without a fight.")
                                print("The glass cracks under the force of your shoulder, and having seen this, you start to repeatedly bash the glass, the sound and the rapid footsteps of whatever monster was after you getting closer by the second.")
                                print("The glass eventually breaks, the massive difference in pressure immediately sucking you out into space sending you hurdling into space as the integrity of the inside of the facility was torn to shreds.")
                                print("The view was suddenly interrupted by the grip of whatever was chasing you. Your eyes meet with the seemingly humanoid figure in a space suit gripping your shoulder tightly, but it's already very apparent that this is not a human.")
                                print("The planet below may have been from where this abomination came from, which made everything clear. Your adrenaline fueled body was already in a fight or flight response as you take your last lucky roll of the dice.")
                                print("It's time you turned the tables.")
                                print("BASH/BASH")

                                do = input(":: ")
                                if do == "BASH":
                                    print("You bash the mimicing monster in the visor with your elbow, knocking it off of you and sending it into the atmosphere of the nearby planet.")
                                    print("It's over. The monster is gone, and you're out in the vaccuum of space. it's only a matter of time before the oxygen in your tank runs out. You're just glad things won't end badly.")
                                    print("TRUE END: Afloat in the Void.")
                                    print("Game made by:")
                                    print("Diego Casillas")
                                    print("Game play-tested by:")
                                    print(name)
                                    print("Thank you for playing my game :)")
                                    end = input("Type END to leave: ")



                elif do == "FACE THE CONCEQUENCES":
                        print("You turn around, taking a deep gulp as you do so. ")
                        print("Standing in front of you seemed to be another figure in a space suit, colored in a shade of red rather than your own white. He looked almost exactly like you, but something about him seemed different... ")
                        print("BAD END 2: The Suspicious one in Red")
                        end = input("Type END to leave: ")

                elif do == "GIVE IN":
                    print("You decide to cave just as you're starting to leave this room behind.")
                    print("The plate seemed to have completely disappeared when you turned around. Your severe disappointment is too overwhelming, and you proceed to fall to the floor. The moment you hit the ground, You're brought back to the caves. It seems that the paths you could have taken has drastically expanded, each route leading you to an inevitable fate that results in your demise. Each time you die, you come back, but with more pointless choises where you just die, over and over again. The nightmare never ends, and you know it.")
                    print("BAD END 1: You've met a terrible fate, haven't you?")
                    end = input("Type END to leave: ")

elif do == "LEFT":
            print("The pathway seems to incline drastically downwards, and the ground seems to transition from stone to ice.")
            print("Your foot slips, causing you to fall face first into a pit. your head violently hits the end, the rest of your limp body following after.")
            print("You're Done. Cause: Severe Trauma to the Head.")
            print("Deceased Identification:")
            print(name)
            end = input("Type END to leave: ")
elif do == "STRAIGHT":
    print("The path seemed safe enough, but the sounds become even louder. The walls begin to twist as your head begins to hurt.")
    print("The sound was replaced by the crumbling of the ground, as the floor gave way to a massive pit of lava. you promptly fall in")
    print("You're Done. Cause: Cremation.")
    print("Deceased Identification:")
    print(name)
    end = input("Type END to leave: ")

question_limit = 8
print("Hello! Please think of a land mammal.")
question_count = 0
guess = ""
guess_status = False
idk = False
while question_count <= question_limit and not guess_status and not idk:
    question_count = 0
    leg = input("Does your animal walk on 4 legs? y/n\n")
    question_count += 1
    if leg == "y":
        dairy = input("Is it commonly used to create dairy products? y/n\n")
        question_count += 1
        if dairy == "y":
            fur = input("Does it have fur? y/n\n")
            question_count += 1
            if fur == "y":
                hill = input("Can it commonly be found on hills/mountains? y/n\n")
                question_count += 1
                if hill == "y":
                    guess = "Goat"
                    guess_status = True
                else:
                    guess = "Sheep"
                    guess_status = True
            elif fur == "n":
                farms = input("Can it be found in farms all around the world? y/n\n")
                question_count += 1
                if farms == "y":
                    guess = "Cow"
                    guess_status = True
                else:
                    guess = "Buffalo"
                    guess_status = True
        if dairy == "n":
            fur = input("Does it have fur? y/n\n")
            question_count += 1
            if fur == "y":
                pet = input("Is it a fairly common/regular house pet? y/n\n")
                question_count += 1
                if pet == "y":
                    hunt = input("Does your animal usually hunt for food in the wild? y/n\n")
                    question_count += 1
                    if hunt == "y":
                        doggo = input("Is your animal often seen as mans best friend? y/n\n")
                        question_count += 1
                        if doggo == "y":
                            guess = "Dog"
                            guess_status = True
                        else:
                            guess = "Cat"
                            guess_status = True
                    else:
                        rabbit = input("Is your animal associated with any popular holidays? y/n\n")
                        question_count += 1
                        if rabbit == "y":
                            guess = "Rabbit/Bunny"
                            guess_status = True
                        else:
                            dirty = input("Is it seen as a 'dirty' animal? y/n\n")
                            if dirty == "y":
                                guess = "Rat/Mouse"
                                guess_status = True
                            if dirty == "n":
                                guess = "Guinea Pig/Hamster"
                                guess_status = True
            if fur == "n":
                large = input("Is it larger than a human? y/n\n")
                question_count += 1
                if large == "y":
                    africa = input("Is it (mostly) found in Africa? y/n\n")
                    question_count += 1
                    if africa == "y":
                        danger = input("Is it seen as dangerous to humans? y/n\n")
                        question_count += 1
                        if danger == "y":
                            horn = input("Does it have a horn? y/n\n")
                            if horn == "y":
                                guess = "Rhino"
                                guess_status = True
                            if horn == "n":
                                guess = "Jaguar/Puma/Leopard"
                                guess_status = True
                        if danger == "n":
                            tall = input("Does it have a very long neck? y/n\n")
                            question_count += 1
                            if tall == "n":
                                horn = input("Does it have a/any horn/horns? y/n\n")
                                if horn == "n":
                                    guess = "Elephant"
                                    guess_status = True
                                if horn == "y":
                                    guess = "Antilope"
                                    guess_status = True
                            if tall == "y":
                                guess = "Giraffe"
                                guess_status = True
                    if africa == "n":
                        ride = input("Is it used for transportation? y/n\n")
                        question_count += 1
                        if ride == "y":
                            guess = "Horse"
                            guess_status = True
                        if ride == "n":
                            idk = True
    if leg == "n":
        human = input("Is your animal found in every continent? y/n\n")
        question_count += 1
        if human == "y":
            guess = "Human"
            guess_status = True
        if human == "n":
            australia = input("Is it commonly found in Australia? y/n\n")
            question_count += 1
            if australia == "y":
                guess = "Kangaroo"
                guess_status = True
            else:
                guess = "Monkey/Ape (Primate)"
                guess_status = True

if guess_status:
    print("I think your animal is:" + " " + guess)
elif guess_status or idk:
    print("Hm I cant guess")

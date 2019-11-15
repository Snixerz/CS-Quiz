
print('Welcome to CS Quiz! You will be given 10 questions!')

question_1 = "\033[45mQuestion 1: If you cry in space the tears just stick to your face.\033[0m"
question_2 = "\033[45mQuestion 2: If you cut an earthworm in half, both halves can regrow their body.\033[0m"
question_3 = "\033[45mQuestion 3: Humans can distinguish between over a trillion different smells.\033[0m"
question_4 = "\033[45mQuestion 4: Adults have fewer bones than babies do.\033[0m"
question_5 = "\033[45mQuestion 5: Drinking alcohol kills brain cells.\033[0m"
question_6 = "\033[45mQuestion 6: Humans can’t breathe and swallow at the same time.\033[0m"
question_7 = "\033[45mQuestion 7: The top of the Eiffel Tower leans away from the sun.\033[0m"
question_8 = "\033[45mQuestion 8: It costs the U.S. more to make pennies and nickels than the coins are actually worth.\033[0m"
question_9 = "\033[45mQuestion 9: Goldfish only have a memory of three seconds.\033[0m"
question_10 = "\033[45mQuestion 10: Birds are dinosaurs.\033[0m" 

def answers():
    correct = 0 
    incorrect = 0
    question_number = 1
    if question_number == 1:
        print(question_1)
        guess = input("\033[35mGuess True or False (T/F): \033[0m").lower()
        if guess == "t":
            print("Correct \nYour eyes make tears but they stick as a liquid ball. In other words, astronauts technically can't cry.")
            correct += 1
        elif guess != "t":
            print("Incorrect \nYour eyes make tears but they stick as a liquid ball. In other words, astronauts technically can't cry.")
            incorrect += 1
        question_number += 1
        print(f"You currently have correct \033[32m\033[01m{correct}\033[0m answers, and \033[31m\033[01m{incorrect}\033[0m incorrect answer. Next Question!\n")
    if question_number == 2:
        print(question_2)
        guess = input("\033[35mGuess True or False (T/F): \033[0m").lower()
        if guess == "f":
            print("Correct \nOnly one half of an earthworm can regenerate when its cut in half, not both halves.")
            correct += 1
        elif guess != "f":
            print("Incorrect \nOnly one half of an earthworm can regenerate when its cut in half, not both halves.")
            incorrect += 1
        question_number += 1
        print(f"You currently have correct \033[32m\033[01m{correct}\033[0m answers, and \033[31m\033[01m{incorrect}\033[0m incorrect answer. Next Question!\n")
    if question_number == 3:
        print(question_3)
        guess = input("\033[35mGuess True or False (T/F): \033[0m").lower()
        if guess == "t":
            print("Correct \nIt's not as good as a dog's, but the human nose is still pretty incredible.")
            correct += 1
        elif guess != "t":
            print("Incorrect \nIt's not as good as a dog's, but the human nose is still pretty incredible.")
            incorrect += 1
        question_number += 1
        print(f"You currently have correct \033[32m\033[01m{correct}\033[0m answers, and \033[31m\033[01m{incorrect}\033[0m incorrect answer. Next Question!\n")
    if question_number == 4:
        print(question_4)
        guess = input("\033[35mGuess True or False (T/F): \033[0m").lower()
        if guess == "t":
            print("Correct \nLots of bones (like the cranium) start out as several fragments at birth, then fuse together into a single bone later in life.")
            correct += 1
        elif guess != "t":
            print("Incorrect \nOnly one half of an earthworm can regenerate when its cut in half, not both halves.")
            incorrect += 1
        question_number += 1
        print(f"You currently have correct \033[32m\033[01m{correct}\033[0m answers, and \033[31m\033[01m{incorrect}\033[0m incorrect answer. Next Question!\n")
    if question_number == 5:
        print(question_5)
        guess = input("\033[35mGuess True or False (T/F): \033[0m").lower()
        if guess == "f":
            print("Correct \nDrinking pretty much any non-fatal amount of alcohol won't add enough alcohol to your blood stream to destroy your neurons.")
            correct += 1
        elif guess != "f":
            print("Incorrect \nDrinking pretty much any non-fatal amount of alcohol won't add enough alcohol to your blood stream to destroy your neurons.")
            incorrect += 1
        question_number += 1
        print(f"You currently have correct \033[32m\033[01m{correct}\033[0m answers, and \033[31m\033[01m{incorrect}\033[0m incorrect answer. Next Question!\n")
    if question_number == 6:
        print(question_6)
        guess = input("\033[35mGuess True or False (T/F): \033[0m").lower()
        if guess == "t":
            print("Correct \nIt's because our voice box is lower in the throat than other primates (who can do both at once.) On the plus side, this means we can use language...")
            correct += 1
        elif guess != "t":
            print("Incorrect \nIt's because our voice box is lower in the throat than other primates (who can do both at once.) On the plus side, this means we can use language...")
            incorrect += 1
        question_number += 1
        print(f"You currently have correct \033[32m\033[01m{correct}\033[0m answers, and \033[31m\033[01m{incorrect}\033[0m incorrect answer. Next Question!\n")
    if question_number == 7:
        print(question_7)
        guess = input("\033[35mGuess True or False (T/F): \033[0m").lower()
        if guess == "t":
            print("Correct \nThe metal of the tower expands in the heat of the sun, so the sun-facing side is always slightly bigger than the one facing away – making it lean as much as seven inches away from the sun.")
            correct += 1
        elif guess != "t":
            print("Incorrect \nThe metal of the tower expands in the heat of the sun, so the sun-facing side is always slightly bigger than the one facing away – making it lean as much as seven inches away from the sun.")
            incorrect += 1
        question_number += 1
        print(f"You currently have correct \033[32m\033[01m{correct}\033[0m answers, and \033[31m\033[01m{incorrect}\033[0m incorrect answer. Next Question!\n")
    if question_number == 8:
        print(question_8)
        guess = input("\033[35mGuess True or False (T/F): \033[0m").lower()
        if guess == "t":
            print("Correct \nU.S. taxpayers lost over $100 million in 2013 just through the coins being made.")
            correct += 1
        elif guess != "t":
            print("Incorrect \nU.S. taxpayers lost over $100 million in 2013 just through the coins being made.")
            incorrect += 1
        question_number += 1
        print(f"You currently have correct \033[32m\033[01m{correct}\033[0m answers, and \033[31m\033[01m{incorrect}\033[0m incorrect answer. Next Question!\n")
    if question_number == 9:
        print(question_9)
        guess = input("\033[35mGuess True or False (T/F): \033[0m").lower()
        if guess == "f":
            print("Correct \nGoldfishes' legendarily short memory is a common belief, but it's been debunked repeatedly. They can actually remember things for quite a long time.")
            correct += 1
        elif guess != "f":
            print("Incorrect \nGoldfishes' legendarily short memory is a common belief, but it's been debunked repeatedly. They can actually remember things for quite a long time.")
            incorrect += 1
        question_number += 1
        print(f"You currently have correct \033[32m\033[01m{correct}\033[0m answers, and \033[31m\033[01m{incorrect}\033[0m incorrect answer. Next Question!\n")
    if question_number == 10:
        print(question_10)
        guess = input("\033[35mGuess True or False (T/F): \033[0m").lower()
        if guess == "t":
            print("Correct \nNot all dinosaurs became extinct; some of them survived, and every bird alive today is descended from those survivors.")
            correct += 1
        elif guess != "t":
            print("Incorrect \nNot all dinosaurs became extinct; some of them survived, and every bird alive today is descended from those survivors.")
            incorrect += 1
        question_number += 1
        print(f"You currently have correct \033[32m\033[01m{correct}\033[0m answers, and \033[31m\033[01m{incorrect}\033[0m incorrect answer.\n\033[95m\033[01mThanks for playing!\033[0m")

answers()
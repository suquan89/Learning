import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
num3 = random.randint(1,10)
spin = 0

credit = 100
print("Welcome to SQ's first slot machine!")
print("")

if credit == 0:
    print("You have no Credits. Please game responsibly ")
    quit()

start_of_game = input("Do you wish to roll? (Y/N): ")

if start_of_game.lower() == "n":
    print(f"You decided not to roll. You have {credit} Credits left")
    quit()

while start_of_game.lower() != "y" and "n":
    print(f"Please enter a valid response. You have {credit} Credits left")
    start_of_game = input("Do you wish to roll? (Y/N): ")
    if start_of_game.lower() == "y":
        break
    elif start_of_game.lower() == "n":
        print(f"You decided not to roll. You have {credit} Credits left")
        quit()

if start_of_game.lower() == "y":
    credit -= 10
    spin += 1
    if num1 == num2 == num3:
        credit += 50
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
        """)
        print("JACKPOT!")
    elif num1 == num3:
        credit += 30
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
""")
        print("Not bad!")
    elif num2 == num3:
        credit += 30
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
        """)
        print("Nice roll!")
    elif num1 == num2 :
        credit += 30
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
        """)
        print("Getting hot!")
    else:
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
        """)
        print("So close :(")

while credit >= 10:
    print("")
    cont = input("Continue? (Y/N): ")
    if cont.lower() == "n":
        print(f"You decided not to roll. You have {credit} Credits left")
        print(f"You played {spin} times")
        quit()
    while cont.lower() != "y" and "n":
        print(f"Please enter a valid response. You have {credit} Credits left")
        cont = input("Continue? (Y/N): ")
        if cont.lower() == "n":
            print(f"You decided not to roll. You have {credit} Credits left")
            quit()
        else:
            continue

    credit -= 10
    spin += 1
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    if num1 == num2 == num3:
        credit += 50
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
            """)
        print("JACKPOT!")
    elif num1 == num3:
        credit += 30
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
    """)
        print("Not bad!")
    elif num2 == num3:
        credit += 30
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
            """)
        print("Nice roll!")
    elif num1 == num2:
        credit += 30
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
            """)
        print("Getting hot!")
    else:
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
            """)
        print("Almost :(")

if credit == 0:
    print(f"""
Out of Credits! :(
 
You played {spin} times. 

Please game responsibly :)
    """)

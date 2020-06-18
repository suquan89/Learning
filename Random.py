import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
num3 = random.randint(1,10)

credit = 100

start_of_game = input("Do you wish to roll? (Y/N): ")

if credit == 0:
    print("Out of Credits. Sorry")
    quit()

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
    if num1 == num2 == num3:
        credit += 50
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
        """)
    elif num1 == num3:
        credit += 30
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
""")
    elif num2 == num3:
        credit += 30
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
        """)
    elif num1 == num2 :
        credit += 30
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
        """)
    else:
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
        """)

while credit >= 10:
    cont = input("Continue? (Y/N): ")
    if cont.lower() == "n":
        print(f"You decided not to roll. You have {credit} Credits left")
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
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    if num1 == num2 == num3:
        credit += 50
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
            """)
    elif num1 == num3:
        credit += 30
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
    """)
    elif num2 == num3:
        credit += 30
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
            """)
    elif num1 == num2:
        credit += 30
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
            """)
    else:
        print(f"""
|{num1}|, |{num2}|, |{num3}|, Credits: {credit}
            """)

if credit == 0:
    print("Out of Credits!")
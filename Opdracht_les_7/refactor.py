# Ordering at Mac Donald's
eat_in = False

print("Welkom bij de Mac Donald's")

def ask_question(question, valid_answers):
    question_str = input(question)
    question_upper = question_str.upper()
    while question_upper not in valid_answers:
        question_str = input(question)
        question_upper = question_str.upper()
    return question_upper

def get_burger_choice():
    valid_answer = ask_question("Burgers [Hamburger, Cheeseburger, Big Mac, Quarter Pounder]: ",
                          ("HAMBURGER", "CHEESEBURGER", "BIG MAC", "QUARTER_POUNDER"))
    if valid_answer == "HAMBURGER":
        print("Hamburger")
    elif valid_answer == "CHEESEBURGER":
        print("Cheeseburger")
    elif valid_answer == "BIG MAC":
        print("Big Mac")
    elif valid_answer == "QUARTER POUNDER":
        print("Quarter Pounder")

def get_hot_drink_choice():
    valid_answer = ask_question("Warme drank: [Koffie, Cappucino, Chocolademelk]: ",
                          ("KOFFIE", "CAPPUCINO", "CHOCOLADEMELK"))
    if valid_answer == "KOFFIE":
        print("Koffie")
    elif valid_answer == "CAPPUCINO":
        print("Cappucino")
    elif valid_answer == "CHOCOLADEMELK":
        print("Chocolademelk")


def get_cold_drink_choice():
    valid_answer = ask_question("Koude drank: [Coca Cola, Cola Zero, 7-Up, Fanta, Fristi]: ",
                          ("COCA COLA", "COLA ZERO", "7-UP", "FANTA", "FRISTI"))
    if valid_answer == "COCA COLA":
        print("Coca Cola")
    elif valid_answer == "COLA ZERO":
        print("Cola Zero")
    elif valid_answer == "7-UP":
        print("7-Up")
    elif valid_answer == "FANTA":
        print("Fanta")
    elif valid_answer == "FRISTI":
        print("Fristi")

answer = ask_question("Hier opeten of meenemen? [Opeten/Meenemen]: ",
             ("OPETEN", "MEENEMEN"))

if answer == "OPETEN":
    # Eat in part
    print("Hier opeten")
    eat_in = True
elif answer == "MEENEMEN":
    # Take away part
    print("Meenemen")
    eat_in = False

answer = ask_question("Burgers of drankjes? [Burgers/Drankjes]: ",
             ("BURGERS", "DRANKJES"))

if answer == "BURGERS":
    get_burger_choice()
elif answer == "DRANKJES":
    answer = ask_question("Drankjes [Warme/Koude]: ",
                          ("WARME", "KOUDE"))
    if answer == "WARME":
        get_hot_drink_choice()

    elif answer == "KOUDE":
        get_cold_drink_choice()

if eat_in:
    print("Bedankt voor uw bestelling en eet smakelijk in ons restaurant.")
else:
    print("Bedankt voor uw bestelling, goede reis en eet smakelijk.")
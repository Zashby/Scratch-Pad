#Idea phase
"""
API usage



Maybe meal DB to add a random meal to your dinner calander on google calendar

Random NPC generator for DND, maybe a madlib like story generator to go with it"""

"""
Roadmap:
Basic interface [x]
save weekly menu [x]

--create user profile
----remember preferences
----save favorite meals
----change name
allow user to input save directory [ ]
change API to edamam [ ]
--additional customization
update formatting [ ]
--breakpoints between ingredient - instructions to make it easier to read on terminal
allow user more selection [ ]
implement google calendar [ ]
create shopping list option w/ all required ingredients for week [ ]


"""


import requests
import ast

def striplist(texts):
    from string import punctuation
    punc = list(punctuation) + [" ", "\n", "\r"]
    for x in punc:
        texts = texts.replace(x, "")
    return texts

def meal_prep_format():
    intake = requests.get(f'https://www.themealdb.com/api/json/v1/1/random.php').json()['meals'][0]
    intake = {key:value for key, value in intake.items() if (value != '' and value != ' ' and value != None)}

    return intake

def meal_prep(meal):
    print(f"\nLets cook some {meal['strMeal']}\n")
    
    print("Here are the ingredients you will need!")
    for x in range(1,20):
        try:
            print (meal.get(f"strIngredient{x}") + " " + meal.get(f"strMeasure{x}"))
        except TypeError:
            pass
    pause = input("press enter to continue.")
    print("Here are your handy instructions: \n")
    print(meal["strInstructions"] )
    pause = input("press enter to go back to the main menu chef.")

def main():
    iter_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    week_meals = {}

    # Maybe code for later
    # pull_list = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?a=list').json()['meals']
    # area_list = [x["strArea"] for x in pull_list]
    # type_list = [x for x in random.choice()]
    with open(".chef_text.txt", "w") as f:
        read_file = f.read()
    week_meals = ast.literal_eval(read_file)
    while True:
    
        print(f"""
        Hello! Trying to cook more? Let me help you!
        Please pick one of the following options:

        1. See your list
        2. Build a new list
        3. Pick a day
        4. Ingredients list for the week
        5. Exit
        """)
        try:
            cook_choice = int(input("What will it be, chef: "))
        except (TypeError, ValueError):
            print("I am afraid I do not understand chef... let's try again")
            continue
        if cook_choice == 1:
            print("\n")
            if len(week_meals)>0:
                for iter in iter_list:
                    print(iter + " " + week_meals[iter]['strMeal'])
                pause = input("Press enter to continue.")
            else:
                print("Nothing on the books this week chef.")
   
        if cook_choice == 2:
            for iter in iter_list:
                week_meals[iter] = meal_prep_format()
        if cook_choice == 3:
            day = input("Okie dokie chef! Please tell me what day it is: ").lower()
            if day in week_meals.keys():
                print("Alrighty, here we are!")
                meal_prep(week_meals[day])
            else: 
                print("I am afraid I do not have that on the books chef.\n")
        if cook_choice == 4:
            print("\nHere are your ingredients for the week chef!\n")
            for key in week_meals.keys():
                for x in range(1,20):
                    try:
                        print (week_meals[key].get(f"strIngredient{x}") + " " + week_meals[key].get(f"strMeasure{x}"))
                    except TypeError:
                        pass
            pause = input("Press enter to continue.")
        if cook_choice == 5:
            with open("./chef_text.txt", "w+") as f:
                f.write(str(week_meals))
            print("See you next time chef!")
            break

main()






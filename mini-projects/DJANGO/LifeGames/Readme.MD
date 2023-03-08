Hello! I wanted to make something new, so I am starting LifeGames! A way to experiment with various thingies and frameworks to make engaging gameplay style thingies for everyday life.


The project has no real direction aside from boredom and wanting to work on something besides VertManager.

App # 1 MealDeck

The intent is to create a kind of engaging and quirky way to schedule meals and consolidate necessary information regarding cooking. The basic cycle will work as follows:
-At the beginning of the month a "deck" will be created from 60 recipes (pulled from edamam's API database (thanks dudes!))
-User draws 7 breakfast, 7 lunch, and 7 dinner cards at the beginning of the week (7 max, less acceptable)
    -User will be able to move cards around and whatnot or select a certain number of cards to return to their respective decks and redraw
-After finalizing selections, user is given a recipe breakdown per meal and per week (for shopping purposes)
-User will have a "play" area which will allow them to take their card of choice, place on the play area, and generate the specifics regarding that meal (ingredients, instructions, etc.)


Work Breakdown:
[] Build basic models
    [] recipe "deck"
    [] recipe "card"
    [] user
        [] profile
        [] game mechanic specifics
        [] a streak obviously because people like big numbers
    [] additional
[] Build API pull requests for edamam API (hide key >.>)
    [] Learn about API request structure of edamam
    [] recipe / dietary preferences 
[] Build game board 
    [] Draggable cards
    [] Various play area elements


[] Have a good cry
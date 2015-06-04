#-----------------------#
# Michael Beaver        #
# 3 June 2015           #
#-----------------------#
# pyku Haiku Generator  #
#                       #
# Basic (pseudo)random  #
# haiku generator. Words#
# collected from various#
# places on Internet.   #
#-----------------------#

import random

#---------------------------------------------------------

words = [["oft", "Sun", "bus", "few", "act", "bid", "red", "one", "cat", "raid", "dumb", "moon", "slew", "life", "base", "head", "plot", "high", "soul", "fear", "love", "week", "head", "rage", "base", "door", "drop", "yard", "heat", "pole", "cord", "vile", "path", "step", "sack", "soul", "week", "high", "fear", "sword", "steel", "sweep", "tongue", "wrong", "spoke", "cause", "worse", "crown", "blame", "mourn", "scene", "break", "dumb", "faith", "count", "glove", "steep", "knees", "snake", "pause", "month", "bomb", "month", "cheeks", "yelled", "tongue", "school"],
         ["rhythm", "baby", "bacon", "balloon", "baseball", "bedroom", "bedtime", "berry", "body", "bunny", "butter", "button", "good-bye", "neighbor", "rabbit", "bathtub", "pancake", "paper", "pencil", "people", "pizza", "popcorn", "pepper", "sleeping", "toothpaste", "zip code", "zipper", "bus stop", "ketchup", "syrup", "table", "teacher", "tired", "toilet", "tonight", "towel", "closet", "doctor", "dinner", "birthday", "reading", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sunday", "farmer", "finger", "forehead", "breakfast", "vacuum", "vowel", "color", "cookie", "napkin", "weekend", "music", "stomach", "April",  "August", "yellow", "purple", "seven", "circle", "oval", "shampoo", "shoulder", "shower", "ocean", "tissue", "toothbrush", "cherry", "kitchen", "inches", "question", "sandwich", "brother", "sister", "father", "mother", "garbage", "number", "wagon", "manners", "woman", "bathroom", "window", "happy", "hot dog", "scissors", "lying", "scary", "surprise", "airplane", "asleep", "apple", "clothing", "address", "uncle", "frozen", "afraid", "spelling", "grandma", "grandpa"],
         ["Dragonborn", "basketball", "bicycle", "blueberry", "broccoli", "neighborhood", "library", "umbrella", "principal", "privacy", "apricot", "piano", "potato", "piggybank", "policeman", "envelope", "telephone", "tortilla", "screwdriver", "beautiful", "computer", "hospital", "tomato", "chocolate", "parking lot", "spaghetti", "spider web", "dangerous", "dinosaur", "grandmother", "grandfather", "grasshopper", "lemonade", "tricycle", "post office", "fingernail", "butterfly", "littlest", "slippery", "video", "vitamin", "government", "camera", "gas station", "category", "gigantic", "ladybug", "toothbrushes", "sandwiches", "bathing suit", "imagine", "coloring", "handwriting", "another", "banana", "ice cream cone", "magazine", "marshmallow", "animal", "microwave", "New Year's Day", "history", "hamburger", "unhappy", "newspaper", "president", "apple juice", "celery", "bologna", "roller skates", "tomorrow", "pajamas", "Saturday", "September", "October", "November", "December", "rectangle"],
         ["anybody", "obedient", "celebration", "librarian", "discovery", "roller skating", "discovery", "impossible", "invisible", "vegetable", "questionable", "appreciate", "vice president", "peanut butter", "police station", "potato chips", "apologize", "paper towel", "supermarket", "vice principal", "chocolate chip", "tomato soup", "telephone book", "television", "temperature", "vacuum cleaner", "salad dressing", "alligator", "baby sitter", "calculator", "elevator", "escalator", "thermometer", "historical", "motorcycle", "dandelion", "asparagus", "grand piano", "video game", "congratulate", "misunderstand", "understanding", "cauliflower", "photographer", "avocado", "poison ivy", "caterpillar", "kindergarten", "cooperate", "conversation", "dictionary", "area code",  "macaroni", "chocolate cake", "raspberry bush", "strawberry bush", "tortilla chips", "barbecue chips", "jack in the box", "gymnasium", "gingerbread man", "refrigerate", "horseback riding", "mountain climbing", "banana split", "hot-air balloon", "America", "washing machine", "watermelon", "unicycle", "helicopter", "alphabetize", "musical chairs", "vitamin C", "tomato juice", "January", "February"],
         ["planetarium", "personality", "pledge of allegiance", "hippopotamus", "denominator", "potato salad", "refrigerator", "saltwater taffy", "alphabetical", "mathematical", "disorganization", "disagreeable", "unquestionable", "electricity", "cafeteria", "unforgettable", "vocabulary", "veterinarian", "anniversary", "university", "California", "congratulations", "cooperation", "communication", "South America", "imagination", "apologetic", "elementary", "misunderstanding", "immediately", "condominium", "organization", "disobedient", "vice presidency", "curiosity", "magnifying glass", "laboratory", "auditorium", "vegetarian"]]

#---------------------------------------------------------

def makeLine(syll):
    """Generates a line with syll syllables"""

    line = str()
    if (syll < 1):
        return None
    
    while (syll > 0):
        if (syll == 1):
            x = 1
        else:
            x = random.randrange(1, syll)
        if (x > 5):
            x = random.randrange(1, 5)
        line = line + words[x - 1][random.randrange(0, len(words[x - 1]) - 1)] + " "
        syll = syll - x

    return line

#---------------------------------------------------------

while (True):
    print(makeLine(5))
    print(makeLine(7))
    print(makeLine(5))
    input()

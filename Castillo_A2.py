"""
@Alan Castillo
"""

"""
Part 1
colors: 
red + blue + yellow =   (black) // could not find an exact color since it depends on the shade of red blue and yellow
yellow + red = orange   (divisible by 3 and > 30)
red + blue = purple     (divisible by 2 and > 30)
yellow + blue = green   (divisible by 3 and 2)
blue                    (divisible by 2)
yellow                  (divisible by 3)
red                     (> 30)
white                   otherwise
"""
number = 36
print(number)
if number % 2 == 0 and number % 3 == 0 and number > 30:
    print("black")
elif number % 2 == 0 and number % 3 == 0:
    print("green")
elif number % 3 == 0 and number > 30:
    print("orange")
elif number % 2 == 0 and number > 30:
    print("purple")
elif number % 2 == 0:
    print("blue")
elif number % 3 == 0:
    print("yellow")
elif number > 30:
    print("red")
else:
    print("white")

"""
Part 2
"""

donutdict = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "batters": {
        "batter":
        [
            { "id": "1001", "type": "Regular" },
            { "id": "1002", "type": "Chocolate" },
            { "id": "1003", "type": "Blueberry" },
            { "id": "1004", "type": "Devil's Food" }
        ]
    },
    "topping": [
        { "id": "5001", "type": "None" },
        { "id": "5002", "type": "Glazed" },
        { "id": "5005", "type": "Sugar" },
        { "id": "5007", "type": "Powdered Sugar" },
        { "id": "5006", "type": "Chocolate with Sprinkles" },
        { "id": "5003", "type": "Chocolate" },
        { "id": "5004", "type": "Maple" }
    ]
}

#2.1
for batterType in donutdict['batters']['batter']:
    for toppingType in donutdict['topping']:
        print(batterType['type'], toppingType['type'])

#2.2 this is assuming the isntruction means only chocolate batters and not chocolate toppings
for batterType in donutdict['batters']['batter']:
    if batterType['type'] == 'Chocolate' or batterType['type'] == "Devil's Food":
        for toppingType in donutdict['topping']:
            print(batterType['type'], toppingType['type'])
    

"""
Part 3
"""
cleanData  = {'people':[]}
messyData = "Name,Age,Occupation;Helen,32,teacher;Ajan,24,Analyst;Jasmine,27,Engineer"
#convert string into a 2D array
strArr = messyData.split(";")
wordSplit = []
for x in strArr:
    word = x.split(",")
    wordSplit.append(word)

#convert each array into a dictionary
for i in range(1,4):
    my_dict = {}
    for j in range(0, 3):
        if j == 0:
            my_dict['name'] = wordSplit[i][0]
        elif j == 1:
            my_dict['age'] = int(wordSplit[i][1])
        else:
            my_dict['occupation'] = wordSplit[i][2]
    #append dictionary to people array
    cleanData['people'].append(my_dict)

print(cleanData)


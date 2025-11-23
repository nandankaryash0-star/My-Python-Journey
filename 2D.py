#fruits = ["apple","coconut","avacardo","banana","orange"]
#vegetable = ["cauliflower","carrot","potatoes","tomato","spinach" ]
#meat = ["chicken","mutton","fish"]

groceries = [["apple","coconut","avacardo","banana","orange"],
             ["cauliflower","carrot","potatoes","tomato","spinach" ],
             ["chicken","mutton","fish"]]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
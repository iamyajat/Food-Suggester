def addRecipe():
    fr = open("recipes\\num_of_recipes.txt", "r")
    rno = int(fr.read())+1
    fr.close()
    rname = input("Enter the name of the recipe: ")
    numofing = int(input("Enter the number of ingredients: "))
    ing = ""
    print("Enter the ingredients: ")
    for i in range(numofing):
        ing += input().lower()+"\n"
    strtosave = rname+"\n"+ing
    fw = open("recipes\\"+str(rno)+".txt", "w")
    fw.write(strtosave)
    fw.close()
    fw = open("recipes\\num_of_recipes.txt", "w")
    fw.write(str(rno))
    fw.close()
    print("\nAdded\n\n")


def addAvailableIngredients():
    fr = open("items\\available_ingredients.txt", "r")
    ing = fr.readlines()
    ing.append(input("Enter the name of the ingredient: ").lower()+"\n")
    fr.close()
    ings = ""
    for i in set(ing):
        ings += i
    f = open("items\\available_ingredients.txt", "w")
    f.write(ings)
    f.close()
    print("\nAdded\n\n")

def showAvailableIngredients():
    print("\nAvailable Ingredients:\n")
    fr = open("items\\available_ingredients.txt", "r")
    ings = fr.readlines()
    fr.close()
    for ing in ings:
        print(ing, end="")
    print("\n\n")


def deleteIngredient():
    fr = open("items\\available_ingredients.txt", "r")
    ings = fr.readlines()
    fr.close()
    delitem = input("Enter the ingredient to be removed: ").lower()+"\n"
    if delitem in ings:
        ings.remove(delitem)
        ing = ""
        for i in ings:
            ing += i
        f = open("items\\available_ingredients.txt", "w")
        f.write(ing)
        f.close()
    else:
        print("Ingredient not present")
    print("\nRemoved\n\n")

def suggestRecipe():
    print("\nYou can make:\n")
    fr = open("items\\available_ingredients.txt", "r")
    ings = fr.readlines()
    fr.close()

    fr = open("recipes\\num_of_recipes.txt", "r")
    rno = int(fr.read())
    fr.close()

    for i in range(1, rno+1):
        fr = open("recipes\\"+str(i)+".txt", "r")
        rec = fr.readlines()
        fr.close()

        show = True
        for j in range(1, len(rec)):
            if rec[j] not in ings:
                show = False
                break
        if show:
            print(rec[0],end="")
    print("\n\n")


print("\n\nWELCOME TO THE RECIPE SUGGESTER APP\n")

while True:
    print("Choose: ", "1. Add Recipe", "2. Add Available Ingredients", "3. Remove An Ingredient",
          "4. Show Available Ingredients", "5. Suggest a Recipe", "Press any other key to exit.", sep="\n")
    opt = input()
    if opt=="1":
        addRecipe()
    elif opt=="2":
        addAvailableIngredients()
    elif opt=="3":
        deleteIngredient()
    elif opt=="4":
        showAvailableIngredients()
    elif opt=="5":
        suggestRecipe()
    else:
        break
print("Thank you for using this app. Have a great day!")
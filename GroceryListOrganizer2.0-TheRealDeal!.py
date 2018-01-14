store = {"produce":["potatoes", "carrots", "lettuce", "romaine", "arugala", "mushrooms",
           "apples", "brussels sprouts", "peppers", "asparagus", "cucumbers", "broccoli", "pomegranate"],

         "dairy and eggs":["eggs", "milk", "yogurt", "fage", "cheddar",
                  "creamcheese", "butter", "heavy whipping cream",
                  "heavy cream", "buttermilk", "half and half", "cream"],
         
         "cheese and meat":["chicken", "pork", "beef", "turkey", "bacon",
                   "turkey bacon", "ground beef", "hot dogs"],

         "aisle_one":[],

         "aisle_two":[],
}


groceries = []
sorteddict = {"produce":[], "dairy and eggs":[], "cheese and meat":[], "aisle_one":[], "aisle_two":[]}
#length = int(input("How many items do you need? "))
##################################################################

#Welcome and explaining the commands:
print("Hello!  Welcome to your handy dandy grocery list organizer for Wegmans in Ithaca, NY!")
print("")
print("Okay, just list the items on your grocery list below in any old order.  They should",
        " be all lower case and not include the amount of the item that you need.  Hit 'enter' after listing an item.")
print("When you are done listing all your items, just write 'done' and hit enter to have your list sorted!")
print("")

def askforinput():
    
    def appenditem(z):
        groceries.append(z)
        
    x = input("")
    
    if x != "done":
        appenditem(x)
        askforinput()
    elif x == "done":
        q = input("Are you sure that's everything on your list? Y or N?")
        if q == "Y":
            return groceries
        elif q == "N":
            askforinput()
    return groceries
    
#This function takes the grocery list as input by user, organizes it,
#then prints it out under the appropriate headings
def organize_list(lst):
    print(" ")
    print("Okay, here is your grocery list sorted by section of Wegmans: ")
    print("")
    for item in lst:
        if item in store["produce"]:
            sorteddict["produce"].append(item)
        if item in store["dairy and eggs"]:
            sorteddict["dairy and eggs"].append(item)
        if item in store["cheese and meat"]:
            sorteddict["cheese and meat"].append(item)
    if len(sorteddict["produce"]) > 0:
        print("Produce: ")
        for thingy in sorteddict["produce"]:
            print(thingy)
        print(" ")
    if len(sorteddict["dairy and eggs"]) > 0:
        print("Dairy and Eggs: ")
        for thingy in sorteddict["dairy and eggs"]:
            print(thingy)
        print(" ")
    if len(sorteddict["cheese and meat"]) > 0:
        print("Cheese and Meat: ")
        for thingy in sorteddict["cheese and meat"]:
            print(thingy)
        print(" ")

####################################################################
        
organize_list(askforinput())


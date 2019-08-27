#Shopping List Program
import sys
print("Welcome to a mini Shopping List Program")

#Create a new list named shopping_list
shopping_list = []

#Show help menu
def show_help():
    print("""
Enter 'DONE' to stop adding items
Enter 'HELP' for this HELP
Enter 'VIEW' to see all items in list
""")


#Add item to list
def add_to_list(item):
    shopping_list.append(item)
    print("Added!List has {} item(s)".format(len(shopping_list)))


#Show Items in list
def show_list():
    print("\033[H\033[J")
    print("Your shopping list")
    for item in shopping_list:
        print("* " +item)

show_help() 


print("Please add a new item")
print("")
#Continually prompt user to add item or view list if they need to
while True:
#using raw_input() instead of just input() coz i run my program in python2 and thus it expects me to put quotes around my input
    new_item = raw_input("> ") 
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'VIEW':
        show_list()
        continue
            
        #continue
    add_to_list(new_item)
show_list()







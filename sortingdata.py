# The title of the program
print("Sort data alphabetically!")

# Creating the empty list which will store the names
names = []

# Handling errors
try:
    no_of_names = int(input("Number of words you want to sort out: "))
except ValueError:
    print("Please enter a number.")
    exit()

is_indexed = input("Do you want the names to have index numbers? y/n: ").lower()
if is_indexed != 'y' and is_indexed != 'n':
    print("You have entered incorrect info. The names will have indexes as default.")
    is_indexed = 'y'

# Getting inputs from the user inside the loop
for i in range(no_of_names):
    name = input("Please enter a name: ")
    if name == 'exit':
        break
    else:
        # Adding the name to the empty list (in lower case)
        names.append(name.lower())

# Printing the final result
print("\nNames sorted out alphabetically: ")
counter = 1
for name in sorted(names):
    if is_indexed == 'y':
        print(str(counter) + '.' + name.title())
    else:
        print(name.title())
    counter += 1

# The program is done!
print("\nDone!")

name = input("Enter a name ")
names = ("Griffin","Daniel","Jimmy","Ian","Samantha","Julia","Tom","Jack")
found = 0
for n in range(8):
    if name == names[n]:
        print("That name is on the list")
        found = 1
        break
if found == 0:
    print ("That name is not on the list")

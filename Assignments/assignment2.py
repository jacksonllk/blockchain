# Initializing our name list
namelist = ["Nolan", "Jeremy", "Dylan", "Patricia", "Alexander", "Adam", "Nairobi", "Annabelle"]


for name in namelist:
    if (len(name) > 5):
        if ('n' in name) or ('N' in name):
            print(name)


while len(name) >= 1:
    namelist.pop()
    print(namelist)
    if len(namelist) == 0:
        print("List Emptied!")
        break


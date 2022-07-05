
age = int(input("enter your age: "))


def decades_lived(age):
    return age//10


decades = "You have lived " + str(decades_lived(age)) + " decades"

print(decades)

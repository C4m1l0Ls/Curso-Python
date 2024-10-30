
cc = True

while cc:

    age = int (input("cual es su edad ?: "))
    country = input ("en que pais vive ? ")

    if age >= 21 and country == "usa":
        print ("usted puede tomar alcohol en usa")
    elif age >= 18 and country =="col":
        print ("usted puede tomar alcoholen col")
    else:
        print("usted no puede tomar alcohol")

        for i in range(10):
            print (i)
            
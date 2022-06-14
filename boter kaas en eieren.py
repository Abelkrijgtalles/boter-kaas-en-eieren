gebruiker = "X"

def anderegebruiker(gebruiker):
    if gebruiker == "X":
        gebruiker = "O"
    else:
        gebruiker = "X"
    return gebruiker

rij1 = ["-", "-", "-"]
rij2 = ["-", "-", "-"]
rij3 = ["-", "-", "-"]

def zetzet(getal, gebruiker):
    getal = getal - 1

    if getal < 3:
        if rij1[getal] == "X" or rij1[getal] == "O":
            print("Er is al een zet gedaan op die plek, dus kan je niet daar je zet zetten")
        else:
            rij1[getal] = gebruiker
            checkwin(gebruiker)
    if getal <= 5 and getal > 2:
        if rij2[getal - 3] == "X" or rij2[getal - 3] == "O":
            print("Er is al een zet gedaan op die plek, dus kan je niet daar je zet zetten")
        else:
            rij2[getal - 3] = gebruiker
            checkwin(gebruiker)
    if getal <= 8 and getal >= 5:
        if rij3[getal - 6] == "X" or rij3[getal - 6] == "O":
            print("Er is al een zet gedaan op die plek, dus kan je niet daar je zet zetten")
        else:
            rij3[getal - 6] = gebruiker
            checkwin(gebruiker)

def checkwin(gebruiker):
    if rij1[0] == gebruiker and rij2[1] == gebruiker and rij3[2] == gebruiker:
        print(gebruiker, "heeft gewonnen!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        quit()
    elif rij1[2] == gebruiker and rij2[1] == gebruiker and rij3[0] == gebruiker:
        print(gebruiker, "heeft gewonnen!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        quit()
    elif rij1[0] == gebruiker and rij2[0] == gebruiker and rij3[0] == gebruiker:
        print(gebruiker, "heeft gewonnen!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        quit()    
    elif rij1[1] == gebruiker and rij2[1] == gebruiker and rij3[1] == gebruiker:
        print(gebruiker, "heeft gewonnen!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        quit()
    elif rij1[2] == gebruiker and rij2[2] == gebruiker and rij3[2] == gebruiker:
        print(gebruiker, "heeft gewonnen!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        quit()
    elif rij1[0] == gebruiker and rij1[1] == gebruiker and rij1[2] == gebruiker:
        print(gebruiker, "heeft gewonnen!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        quit()    
    elif rij2[0] == gebruiker and rij2[1] == gebruiker and rij2[2] == gebruiker:
        print(gebruiker, "heeft gewonnen!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        quit()
    elif rij3[0] == gebruiker and rij3[1] == gebruiker and rij3[2] == gebruiker:
        print(gebruiker, "heeft gewonnen!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        quit()    

while True:
    print(rij1[0],rij1[1],rij1[2])
    print(rij2[0],rij2[1],rij2[2])
    print(rij3[0],rij3[1],rij3[2])
    print(gebruiker, "is")
    print("1 2 3\n4 5 6\n7 8 9")
    zet = input(gebruiker + " wat is je zet")
    zetzet(int(zet), gebruiker)
    gebruiker = anderegebruiker(gebruiker)
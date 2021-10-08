pocket = int (input("Enter pocket's number:"))

if pocket == 0:
    print ("GREEN")
elif (pocket >= 1 and pocket<=10) or (pocket >= 19 and pocket<=28):
    if pocket % 2 == 0:
        print ("BLACK")
    else:
        print ("RED")
elif (pocket >= 11 and pocket<=18) or (pocket >= 29 and pocket<=36):
    if pocket % 2 == 0:
        print ("RED")
    else:
        print ("BLACK")
else:
    print("INVALID POCKET")
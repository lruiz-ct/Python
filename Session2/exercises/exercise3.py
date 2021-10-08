age = int (input("Enter your age:"))
if age <= 1:
    print("INFANT")
elif age < 13:
    print ("CHILD")
elif age < 20:
    print ("TEENAGER")
else:
    print ("ADULT")
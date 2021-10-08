rectangle1_width = float (input("Enter Rectangle 1 width:"))
rectangle1_height = float (input("Enter Rectangle 1 height:"))

rectangle2_width = float (input("Enter Rectangle 2 width:"))
rectangle2_height = float (input("Enter Rectangle 2 height:"))

rectangle1_area = rectangle1_width * rectangle1_height
rectangle2_area = rectangle2_width * rectangle2_height

if rectangle2_area == rectangle1_area:
    print ("The areas of both rectangles are the same")
elif rectangle2_area<rectangle1_area:
    print ("The area of Rectangle 1 is bigger")
else:
    print ("The area of Rectangle 2 is bigger")
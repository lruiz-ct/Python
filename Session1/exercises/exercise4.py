item1 = float(input("item 1:"))
item2 = float(input("item 2:"))
item3 = float(input("item 3:"))
item4 = float(input("item 4:"))
item5 = float(input("item 5:"))

subtotal = item1 + item2 + item3 + item4 + item5
tax = subtotal * .07
total = subtotal + tax

print(f"subtotal: {subtotal:.2f}")
print(f"tax: {tax:.2f}")
print(f"total: {total:.2f}")

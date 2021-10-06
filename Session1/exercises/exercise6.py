amount = float (input("Enter total amount of purchase:"))
state_tax = amount * .05
country_tax = amount * .025


print(f"State tax: {state_tax:.2f}")
print(f"Country tax: {country_tax:.2f}")
print(f"Total taxes: {state_tax + country_tax:.2f}")
print(f"Total Sale: {amount+state_tax + country_tax:.2f}")
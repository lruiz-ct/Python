# This program demonstrates the repetition operator.

def main():
    # Print nine rows increasing in length.
    for count in range(1, 10):
        print('Zi' * count)


    # Print nine rows decreasing in length.
    for count in range(8,0,-1):
        print('Zv' * count)

# Call the main function.
main()
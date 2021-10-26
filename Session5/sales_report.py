# This program displays the total of the
# amounts in the sales_data.txt file.

def main():
    # Initialize an accumulator.
    total = 0.0

    try:
        # Open the sales_data.txt file.
        infile = open('sales_222.txt', 'r')

        # Read the values from the file and
        # accumulate them.  
        for line in infile:
            amount = float(line)
            total += amount

        # Close the file.
        infile.close()

        # Print the total.
        print(f'{total:,.2f}')

    except IOError as error:
        print('An error occured trying to read the file.'+ str(error))
    except ValueError:
        print('Non-numeric data found in the file.')
    except:
        print("An error ocurred")
    print('Program finished correctly')

main()
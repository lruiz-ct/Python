def main():
    # Create a string with a date.
    date_string = '11/26/2020'

    # Split the date.
    date_list = date_string.split('/')

    # Display each piece of the date.
    print(f'Month: {date_list[0]}')
    print(f'Day: {date_list[1]}')
    print(f'Year: {date_list[2]}')

main()
MIN_SALARY = 10000
MIN_YEARS = 3

# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

# Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' + 
            'years employed: '))

if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print(f'You must have been employed '
f'for at least {MIN_YEARS} '
f'years to qualify.')
else:
    print(f'You must earn at least $'
f'{MIN_SALARY:,.2f} '
f'per year to qualify.')
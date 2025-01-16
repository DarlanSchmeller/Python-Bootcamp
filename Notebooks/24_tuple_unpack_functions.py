stock_prices = [('APPL',200), ('Google', 400)]

for stock, price in stock_prices:
    print(price + (0.1*price)) # Shows what a 10% increase in price would look like
    print(stock, price)

print('--------------------------------')
work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]

def employee_check(work_hours):
    """
    Iterates through a list containing Tuples
    and returns the employee with the most
    hours worked
    """
    current_max = 0
    employee_of_month = None

    for employee, hours in work_hours:
        if current_max < hours:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return (employee_of_month, current_max)

print(employee_check(work_hours))
employee_of_month, max_hours = employee_check(work_hours) # We can perform Tuple Unpacking on variable assignment
print(f'The employee of the month is {employee_of_month} with {max_hours} hours.')
def calculate_monthly_payment(vehicle_price, apr, loan_term, down_payment, trade_in_value):
    """
    Calculates the monthly payment for a vehicle loan.

    This function calculates the monthly payment required for a vehicle loan based on
    the total vehicle price, annual percentage rate (APR), loan term, down payment, 
    and trade-in value. It accounts for situations where the interest rate is 0%.

    Parameters:
    vehicle_price (float): The total price of the vehicle.
    apr (float): Annual percentage rate of the loan.
    loan_term (int): The loan term in months.
    down_payment (float): The down payment amount.
    trade_in_value (float): The trade-in value of a previous vehicle.

    Returns:
    float: The calculated monthly payment for the vehicle loan.
    """

    loan_amount = vehicle_price - down_payment - trade_in_value
    interest_rate = apr / 1200

    if interest_rate != 0:
        monthly_payment = loan_amount * interest_rate / (1 - (1 + interest_rate) ** (-loan_term))
    else:
        monthly_payment = loan_amount / loan_term # if interest rate is 0%
    return monthly_payment

def main():
    """
    Acts as the primary function for the Monthly Car Payment Calculator.

    This function runs a loop that continuously prompts the user to input details
    of the vehicle loan such as the vehicle price, annual interest rate, loan term,
    down payment, and trade-in value. It then calculates the estimated monthly 
    payment using the 'calculate_monthly_payment' function and displays it.
    
    Parameters:
    None

    Returns:
    None: The function has no return value and outputs the result to the console.
    """
    
    print("")
    print("Monthly Car Payment Calculator")
    print("")

    while True:
        vehicle_price = float(input("Enter the vehicle price: $"))
        apr = float(input("Enter the annual interest rate (%): "))
        loan_term = int(input("Enter the loan term (in months): "))
        down_payment = float(input("Enter the down payment: $"))
        trade_in_value = float(input("Enter the trade-in value: $"))

        print("")
        monthly_payment = calculate_monthly_payment(vehicle_price, apr, loan_term, down_payment, trade_in_value)
        print("Your estimated monthly payment is: ${:.2f}".format(monthly_payment))
        print("")

main()
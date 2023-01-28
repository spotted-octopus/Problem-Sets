# Problem Set 01, Part C: Finding the Right Amount to Save Away 

# Initialize Problem Set Givens
semi_annual_raise = 0.07
r = 0.04 
total_cost = 1000000
down_payment = 0.25 * total_cost

# Inputs 
annual_salary_starting = float(input("Enter your annual salary: "))

# Initialize Bisection Variables 
high = 10000
low = 0 
epsilon = 100 
delta = 500 
num_guesses = 0


while abs(delta) >= epsilon: 

    # Initialize Variables 
    annual_salary = annual_salary_starting
    monthly_salary = annual_salary / 12 
    current_savings = 0 
    months = 0 
    base = 1 

    # Bisection Variables 
    guess = (high + low) // 2 

    # Search Variable 
    portion_saved = guess / 10000.0

    # Determine if able to hit savings target within 3 years 
    while current_savings < down_payment and months < 36: 

        if (float(months)/6) > base:
            annual_salary = annual_salary * (1+semi_annual_raise)
            monthly_salary = annual_salary / 12 
            base = base + 1

        months = months+1
        current_savings = current_savings + current_savings * r / 12 + portion_saved * monthly_salary

    delta = current_savings - down_payment

    if delta > epsilon and months <= 36: 
        high = guess 
    else: 
        low = guess 

    num_guesses += 1
    print("high: " + str(high)) 
    print("low: " + str(low))
    print("delta: " +str(delta))

print("Best savings rate: " + str(guess / 10000.0))
print("Steps in bisection search: " + str(num_guesses))

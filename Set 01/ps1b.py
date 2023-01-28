# Problem Set 01, Part B: Saving, with a raise 

r = 0.04 

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25 * total_cost 
monthly_salary = annual_salary / 12 
current_savings = 0 
months = 0 
base = 1 

while current_savings < portion_down_payment: 

    if (float(months)/6) > base:
        annual_salary = annual_salary * (1+semi_annual_raise)
        monthly_salary = annual_salary / 12 
        base = base + 1

    months = months+1
    current_savings = current_savings + current_savings * r / 12 + portion_saved * monthly_salary

print("Number of months: " + str(months))
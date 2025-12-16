


principal = float(input("Enter Loan Amount (principal): "))
rate =      float(input("Enter interest Rate: "))
years =     int(input("Enter loan duration (years): "))


monthly_rate = rate/100/12


# Number of Monthly Payments

num_payments = years * 12

# Loan Payment formula

Monthly_payment =  (principal * monthly_rate) / (1-(1 + monthly_rate) ** -num_payments)

# Outputs 
print("\n ..... Loan Summary...")
print(f"Loan Amount: N{principal:,.2f}")
print(f"Interest Rate: {rate}%")
print(f"Years: {years} years")
print(f"Monthly Payment: N {Monthly_payment:,.2f}")
def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate 
        print(f"year {year}: ${amount:.2f}")

initial_amount = float(input("Initial investment amount: "))
annual_rate = float(input("Annual rate of return (e.g., 0.05 for 5%): "))
num_years = int(input("Number of years: "))

invest(initial_amount, annual_rate, num_years)

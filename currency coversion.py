
exchange_rate = 278.50  # rate
usd = float(input("Enter amount in USD: "))

# Convert USD to PKR
pkr = usd * exchange_rate

print("Equivalent in PKR: Rs", round(pkr, 2))


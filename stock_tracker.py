
import csv

# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Validate number of stocks
while True:
    try:
        num_stocks = int(input("How many different stocks do you want to buy? "))

        if num_stocks > 0:
            break
        else:
            print("Please enter a number greater than zero.")

    except ValueError:
        print("Invalid input! Please enter a whole number.")

# Enter stock details
for i in range(num_stocks):
    print("\nStock", i + 1)

    # Validate stock symbol
    while True:
        stock_name = input("Enter stock symbol: ").strip().upper()

        if stock_name not in stock_prices:
            print("Invalid stock symbol! Choose from the available stocks.")
        elif stock_name in portfolio:
            print("Stock already entered! Please enter a different stock.")
        else:
            break

    # Validate quantity
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                break
            else:
                print("Quantity must be greater than zero.")

        except ValueError:
            print("Invalid quantity! Enter a whole number.")

    portfolio[stock_name] = quantity

    investment = stock_prices[stock_name] * quantity
    total_investment += investment

    print("Investment added:", investment)

# Display portfolio
print("\n===== Your Portfolio =====")

for stock_name, quantity in portfolio.items():
    price = stock_prices[stock_name]
    investment = price * quantity

    print(
        stock_name,
        "| Quantity:", quantity,
        "| Price:", price,
        "| Investment:", investment
    )

print("\nTotal Investment:", total_investment)

# Save portfolio to CSV
save_choice = input("\nDo you want to save your portfolio to CSV? (yes/no): ")

if save_choice.strip().lower() in ["yes", "y"]:
    try:
        with open("portfolio.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Stock Symbol",
                "Quantity",
                "Price",
                "Investment"
            ])

            for stock_name, quantity in portfolio.items():
                price = stock_prices[stock_name]
                investment = price * quantity

                writer.writerow([
                    stock_name,
                    quantity,
                    price,
                    investment
                ])

            writer.writerow([])
            writer.writerow([
                "Total Investment"," ",
                total_investment
            ])

        print("Portfolio saved successfully to portfolio.csv")

    except OSError:
        print("Error: Unable to save the CSV file.")

else:
    print("Portfolio was not saved.")

print("\nThank you for using Stock Portfolio Tracker!")

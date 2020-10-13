from _collections import defaultdict

stocks = defaultdict(int)

while True:
    command = input()
    if command == "statistics":
        break
    product, quantity = command.split(': ')
    stocks[product] += int(quantity)

print("Products in stock:")

for key, value in stocks.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(stocks.keys())}")
print(f"Total Quantity: {sum(stocks.values())}")


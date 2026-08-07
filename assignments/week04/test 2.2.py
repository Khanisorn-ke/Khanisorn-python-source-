prices = []
print("Enter prices of 6 items:")
for i in range(6):
    prices.append(int(input(f"Item {i+1}: ")))

budget = int(input("\nEnter total budget: "))
total = 0
bought = []

for i, price in enumerate(prices, start=1):
    if total + price <= budget:
        total += price
        bought.append(price)
        status = "buy"
    else:
        status = "cannot buy"
    print(f"\nItem {i} = {price} -> {status}")
    print(f"Current total = {total}")

print(f"\nBought items: {bought}")
print(f"Total spent: {total}")
print(f"Remaining budget: {budget - total}")
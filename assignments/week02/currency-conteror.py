# Currency Converter (THB <-> USD)

EXCHANGE_RATE = 35.5  # 1 USD = 35.5 THB

print("Currency Converter")
print("1. THB to USD")
print("2. USD to THB")

choice = input("Choose conversion direction (1 or 2): ")

amount = float(input("Enter the amount to convert: "))

if choice == "1":
    result = amount / EXCHANGE_RATE
    print(f"Formula used: USD = THB / {EXCHANGE_RATE}")
    print(f"{amount:.2f} THB = {result:.2f} USD")
elif choice == "2":
    result = amount * EXCHANGE_RATE
    print(f"Formula used: THB = USD * {EXCHANGE_RATE}")
    print(f"{amount:.2f} USD = {result:.2f} THB")
else:
    print("Invalid choice. Please enter 1 or 2.")
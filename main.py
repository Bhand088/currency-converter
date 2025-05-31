# currency_converter.py

# Dictionary of exchange rates relative to PKR
exchange_rates = {
    "USD": 282.00,
    "EUR": 320.56,
    "GBP": 379.68,
    "INR": 3.27,
    "AED": 76.77,
    "PKR": 1.0  # Base currency
}

def convert_currency(amount, from_currency, to_currency):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("❌ Unsupported currency code.")
        return None

    # Convert amount to PKR
    amount_in_pkr = amount * exchange_rates[from_currency]
    # Convert PKR to target currency
    converted_amount = amount_in_pkr / exchange_rates[to_currency]
    return converted_amount

def main():
    print("🌍 Currency Converter (Updated Rates as of June 1, 2025)")
    print("Supported currencies:", ", ".join(exchange_rates.keys()))

    try:
        amount = float(input("Enter amount: "))
        from_curr = input("From currency code (e.g., USD): ").strip()
        to_curr = input("To currency code (e.g., PKR): ").strip()

        result = convert_currency(amount, from_curr, to_curr)

        if result is not None:
            print(f"✅ {amount} {from_curr.upper()} = {round(result, 2)} {to_curr.upper()}")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()

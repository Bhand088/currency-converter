# simple currency converter

exchange_rates = {
    "USD": 282,
    "EUR": 320,
    "PKR": 1
}

def convert(amount, from_curr, to_curr):
    from_curr = from_curr.upper()
    to_curr = to_curr.upper()

    if from_curr not in exchange_rates:
        print("Currency not supported:", from_curr)
        return
    if to_curr not in exchange_rates:
        print("Currency not supported:", to_curr)
        return

    amount_in_pkr = amount * exchange_rates[from_curr]
    result = amount_in_pkr / exchange_rates[to_curr]

    print(amount, from_curr, "=", round(result, 2), to_curr)

# main
print("Currency Converter")
print("Currencies:", list(exchange_rates.keys()))

amt = input("Amount: ")
from_c = input("From: ")
to_c = input("To: ")

if amt.isnumeric():
    convert(float(amt), from_c, to_c)
else:
    print("Invalid amount")

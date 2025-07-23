import requests

def convert_currency(currencies):

    while True:

        currency = str(input("Enter your base currency and target currency(e.g. USD GBP): ")).upper().split(" ")

        if len(currency) != 2:
            print("Invalid input. Try again.")
            continue

        base, target = currency[0], currency[1]

        if base not in currencies.keys() or target not in currencies.keys():
            print("Invalid choices.")

        else:

            while True:
                try:
                    amount = float(input("Enter your amount: "))
                    break

                except ValueError:
                    print("Please enter a valid number.")
                    continue

            try:
                response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={base}&to={target}")
                result = list(response.json()["rates"].values())[0]
                return base, target, result

            except Exception as e:
                print("Failed to get exchange rate. Try again.", e)
                return None


def get_currency_list(input_currencies_list):
    print("Supported Currencies:")
    print("------------------------")
    for code, name in input_currencies_list.items():
        print(f"{code} - {name}")
    print("------------------------")


def get_history(history):
    print("\n📜 Conversion History:")
    if not history:
        print("No conversions yet.")
    else:
        for base, target in history.items():
            print(f"{base} ➡ {target}")


def main():
    history = {}
    available_currencies = None

    try:
        available_currencies = requests.get("https://api.frankfurter.app/currencies").json()
    except Exception as e:
        print("Failed to get currencies. Try again.", e)

    while True:

        print("\n📋 Main Menu:")
        print("1. 🔁 Convert currencies")
        print("2. 📜 View conversion history")
        print("3. 💱 Show supported currencies")
        print("4. ❌ Exit")

        try:
            option = int(input("What do you want to do?(e.g. 1): "))

        except ValueError:
            print("Please enter a number (1-4).")
            continue

        print("------------------")

        if option == 1:
            base_currency, target_currency, final_result = convert_currency(available_currencies)

            if final_result is None:
                print("Conversion failed. Returning to menu.")
                continue

            print(f"Result: {final_result}")
            history[f"{base_currency} ➡ {target_currency}"] = final_result

        elif option == 2:
            get_history(history)

        elif option == 3:
            get_currency_list(available_currencies)

        elif option == 4:
            break

        else:
            print("Invalid input.")


if __name__ == '__main__':
    main()

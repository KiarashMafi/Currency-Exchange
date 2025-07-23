# 💱 Currency Converter CLI App

This is a simple Python command-line application that converts currencies using the [Frankfurter API](https://www.frankfurter.app/).

## 🚀 Features

- Convert from one currency to another
- View supported currencies and their codes
- Keep a history of conversions within the session
- User-friendly error handling for invalid inputs

## 🛠️ Requirements

- Python 3.x
- `requests` library

You can install the required library using:

```bash
pip install requests
```

## 📦 How to Run

Clone this repository or copy the code into a file, e.g., `converter.py`, and run it using:

```bash
python converter.py
```

## 🧪 Example

```
📋 Main Menu:
1. 🔁 Convert currencies
2. 💱 Show supported currencies
3. 📜 View conversion history
4. ❌ Exit
```

### Sample Input:

```
Enter your base currency and target currency(e.g. USD GBP): USD EUR
Enter your amount: 100
```

### Output:

```
Result: 91.34
```

## 📚 Source API

- Exchange data from [https://www.frankfurter.app/](https://www.frankfurter.app/)

## 📄 License

This project is open for educational use and practice.

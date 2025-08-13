# Currency Converter (Python)

A simple Python script to find the official currency for major countries and to convert amounts between any two listed currencies using live exchange rates.

## Features

- Find the currency used by a country (from a large predefined list)
- Convert an amount from one country's currency to another using real-time rates
- Command-line interface, no extra setup required
- Error handling for unsupported countries/currencies and API issues

## Requirements

- Python 3.6+
- [`requests`](https://pypi.org/project/requests/) library

## Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/0xsoham1/Currency-Converter.git
   cd Currency-Converter
   ```

2. **Install dependencies:**
   ```bash
   pip install requests
   ```

## Usage

1. **Run the script:**
   ```bash
   python currency_converter.py
   ```

2. **Follow the prompts:**
   - Enter the name of the first and second country.
   - The script will show the currency for each country.
   - You can choose to convert a specified amount from the first currency to the second.
   - The script fetches live rates from [open.er-api.com](https://open.er-api.com/).

### Example Session

```
Enter the first country: India
Enter the second country: United States
✅ India uses INR
✅ United States uses USD
Do you want to convert currency? (yes/no): yes
Enter amount in INR: 1000
💱 1000 INR = 12.01 USD
```

## Supported Countries

The script supports a large number of countries across all continents. If a country is not supported, you'll see an error message.

## How It Works

- Looks up the currency code for each country from a built-in dictionary.
- If both countries are recognized, you can opt to convert any amount from the first currency to the second.
- Uses the [open.er-api.com](https://open.er-api.com/) public API for live exchange rates.
- Handles errors such as unsupported countries and network failures gracefully.

## Customization

- To add or modify supported countries, edit the `country_to_currency` dictionary in `currency_converter.py`.
- You can also swap in a different rates API if needed (update the URL in the script).

## License

MIT License

---

*Made with Python and ❤️ by [0xsoham1](https://github.com/0xsoham1)*

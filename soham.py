import requests


country_to_currency = {
    "United States": "USD", "India": "INR", "United Kingdom": "GBP", "Japan": "JPY",
    "Germany": "EUR", "France": "EUR", "Italy": "EUR", "Spain": "EUR", "Portugal": "EUR",
    "Netherlands": "EUR", "Belgium": "EUR", "Austria": "EUR", "Finland": "EUR",
    "Ireland": "EUR", "Greece": "EUR", "Cyprus": "EUR", "Luxembourg": "EUR",
    "China": "CNY", "Russia": "RUB", "Brazil": "BRL", "South Africa": "ZAR",
    "Mexico": "MXN", "South Korea": "KRW", "Turkey": "TRY", "Switzerland": "CHF",
    "Saudi Arabia": "SAR", "Argentina": "ARS", "Nigeria": "NGN", "Indonesia": "IDR",
    "Thailand": "THB", "New Zealand": "NZD", "Singapore": "SGD", "Malaysia": "MYR",
    "Philippines": "PHP", "Vietnam": "VND", "Pakistan": "PKR", "Bangladesh": "BDT",
    "Sri Lanka": "LKR", "Nepal": "NPR", "Afghanistan": "AFN", "Iran": "IRR",
    "Iraq": "IQD", "Israel": "ILS", "UAE": "AED", "Qatar": "QAR", "Kuwait": "KWD",
    "Oman": "OMR", "Bahrain": "BHD", "Egypt": "EGP", "Morocco": "MAD",
    "Algeria": "DZD", "Ethiopia": "ETB", "Kenya": "KES", "Tanzania": "TZS",
    "Uganda": "UGX", "Ghana": "GHS", "Zimbabwe": "ZWL", "Canada": "CAD",
    "Australia": "AUD", "Fiji": "FJD", "Papua New Guinea": "PGK",
    "Chile": "CLP", "Colombia": "COP", "Peru": "PEN", "Paraguay": "PYG",
    "Uruguay": "UYU", "Venezuela": "VES", "Bolivia": "BOB", "Ecuador": "USD",
    "Costa Rica": "CRC", "Panama": "PAB", "Honduras": "HNL", "Nicaragua": "NIO",
    "El Salvador": "USD", "Guatemala": "GTQ", "Cuba": "CUP", "Dominican Republic": "DOP",
    "Haiti": "HTG", "Jamaica": "JMD", "Trinidad and Tobago": "TTD",
    "Barbados": "BBD", "Bahamas": "BSD", "Belize": "BZD"
}

country1 = input("Enter the first country: ").title()
country2 = input("Enter the second country: ").title()

currency1 = country_to_currency.get(country1)
currency2 = country_to_currency.get(country2)

if currency1 is None or currency2 is None:
    print("❌ Sorry, one or both countries are not in the list.")
else:
    print(f"✅ {country1} uses {currency1}")
    print(f"✅ {country2} uses {currency2}")

    choice = input("Do you want to convert currency? (yes/no): ").strip().lower()

    if choice == "yes":
        try:
            amount = float(input(f"Enter amount in {currency1}: "))
            url = f"https://open.er-api.com/v6/latest/{currency1}"
            response = requests.get(url)
            data = response.json()

            if data["result"] == "success":
                rate = data["rates"][currency2]
                converted_amount = amount * rate
                print(f"💱 {amount} {currency1} = {converted_amount:.2f} {currency2}")
            else:
                print("⚠ Error fetching conversion rates.")
        except Exception as e:
            print(f"⚠ An error occurred: {e}")
    else:
        print("✅ Okay, no conversion performed.")



import requests


def fetch_bitcoin_prices():
    try:
        # Fetch the Bitcoin price data
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        # Extract the prices in multiple currencies
        prices = {
            "USD": float(data["bpi"]["USD"]["rate_float"]),
            "EUR": float(data["bpi"]["EUR"]["rate_float"]),
            "GBP": float(data["bpi"]["GBP"]["rate_float"])
        }

        return prices

    except requests.RequestException:
        return None


def calculate_price(prices, amount, currency):
    amount = float(amount)
    coin_price = prices[currency]
    price = amount * coin_price

    # Currency symbol mapping
    currency_symbols = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£'
    }

    currency_symbol = currency_symbols.get(currency, '$')

    return (
        f"The current price per coin in {currency} is {currency_symbol}{coin_price:,.4f}",
        f"The total value of your Bitcoin in {currency} is: {currency_symbol}{price:,.4f}"
    )

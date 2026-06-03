import requests


API_URL = "https://open.er-api.com/v6/latest/"


def get_currency_data(base_currency="USD"):
    try:
        base_currency = base_currency.upper()
        url = API_URL + base_currency

        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("result") != "success":
            return None

        return data

    except Exception as error:
        print("API error:", error)
        return None


def get_all_currencies():
    data = get_currency_data("USD")

    if data is None:
        return []

    currencies = list(data["rates"].keys())
    currencies.sort()

    return currencies


def convert_currency(amount, from_currency, to_currency):
    try:
        amount = float(amount)
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if amount < 0:
            return {"error": "Amount cannot be negative"}

        data = get_currency_data(from_currency)

        if data is None:
            return {"error": "Could not get exchange rates"}

        if to_currency not in data["rates"]:
            return {"error": "Currency not found"}

        exchange_rate = data["rates"][to_currency]
        converted_amount = amount * exchange_rate

        return {
            "amount": round(amount, 2),
            "from_currency": from_currency,
            "to_currency": to_currency,
            "exchange_rate": exchange_rate,
            "converted_amount": round(converted_amount, 2)
        }

    except ValueError:
        return {"error": "Amount must be a number"}


def calculate_profit(cost, selling_price, target_margin):
    try:
        cost = float(cost)
        selling_price = float(selling_price)
        target_margin = float(target_margin)

        if cost < 0 or selling_price < 0:
            return {"error": "Cost and selling price cannot be negative"}

        if selling_price == 0:
            return {"error": "Selling price cannot be zero"}

        if target_margin >= 100:
            return {"error": "Target margin must be less than 100%"}

        profit = selling_price - cost
        margin_percent = (profit / selling_price) * 100

        if cost == 0:
            markup_percent = 0
        else:
            markup_percent = (profit / cost) * 100

        price_for_target_margin = cost / (1 - target_margin / 100)

        return {
            "cost": round(cost, 2),
            "selling_price": round(selling_price, 2),
            "profit": round(profit, 2),
            "margin_percent": round(margin_percent, 2),
            "markup_percent": round(markup_percent, 2),
            "target_margin": round(target_margin, 2),
            "price_for_target_margin": round(price_for_target_margin, 2)
        }

    except ValueError:
        return {"error": "Cost, selling price, and target margin must be numbers"}
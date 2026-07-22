# Currency & Profit Calculator

A compact business utility for currency conversion and margin planning. It keeps two repetitive calculations in one simple interface.

[Open the live application](https://currencycalculatorr.streamlit.app/)

## Features

- Convert between a broad set of currencies using current exchange-rate data
- Calculate profit, margin and markup from cost and selling price
- Find the selling price required to reach a target margin
- Use a lightweight browser interface with no local setup

## Stack

- Python
- Streamlit
- Exchange-rate API integration
- Local rate fallback data

## Run locally

```bash
pip install streamlit requests
streamlit run app.py
```

## Structure

- `app.py` contains the Streamlit interface
- `functions.py` contains conversion and profit-calculation logic
- `rates.json` provides local currency data

## Why I built it

Currency conversion and margin planning are usually handled in separate tools. This project turns both into one fast workflow designed around the decisions a seller makes repeatedly.

Licensed under the MIT License.

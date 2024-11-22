# Product Price Comparison Tool

## Introduction
This tool compares the prices of a product from **Laughs Supermarket** and **Glomark Supermarket**. It fetches product details from the respective websites, extracts the prices, and identifies which supermarket offers the product at a lower price.

## Features
- Fetch product price and name from both supermarkets.
- Parse data from HTML (`Laughs`) and JSON (`Glomark`).
- Display product details and price comparison.
- Highlight the cheaper option or indicate if prices are the same.

## Requirements
1. **Python 3.6+** must be installed.
2. Required Python libraries:
   - `requests`: To fetch web pages.
   - `beautifulsoup4`: For HTML parsing.
   - `json`: For parsing JSON data.

Install the dependencies using:
```bash
pip install requests beautifulsoup4

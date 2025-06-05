# Price Scraper
A simple Python script using Selenium to scrape product prices from multiple e-commerce websites.
Designed to be easily customizable for other websites and price element selectors.

# Features
Scrapes prices from partineh.com and asamkala.com by default.

Automatically falls back to the second site if the product or price is not found on the first.

Uses Selenium with headless Chrome for browser automation.

Easy to customize for any other websites by updating URLs and element selectors.

# How it works
The script takes a list of product codes (item IDs).

It searches the first website (e.g., partineh.com) for each product and tries to find the price using a specific HTML element class or ID.

If the price or product is not found, it tries a second website (e.g., asamkala.com).

Prints the product code and the found price (or a "not found" message).

# Customization
You can customize this script to work with any website by updating:

Search URLs: Change the base URLs in the script to match your target websites’ search query format.

Price element selectors: Update the Selenium selectors (e.g., By.CLASS_NAME, By.ID) to target the correct HTML elements where prices appear on your websites.

Timeouts and error handling: Adjust WebDriverWait times and error catching as needed for site speed and reliability.

# Prerequisites
Python 3.x

Selenium (```pip install selenium```)

Chrome WebDriver (compatible with your installed Chrome version)

# Usage
* Clone this repository or copy the script.

* Update the items list with your product codes.

* Adjust URLs and selectors if you want to scrape other sites.

* Run the script:
```python price_scraper.py```

## Edit
```items = [
    "SY2000-0R4G-S2",
    "SY5000-18G/22P-4",
    #Add more product codes here
]

#Update URLs and selectors inside the script accordingly```

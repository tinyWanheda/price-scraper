# 🔍 Selenium Web Scraper for Partineh & Asamkala

This Python script uses Selenium to search for a list of product model numbers on two Iranian e-commerce websites: [Partineh](https://partineh.com) and [Asamkala](https://asamkala.com). It attempts to find each product and extract its price if available, saving the results in a `result.txt` file.

---

## 🚀 Features

- Searches for a list of items on both websites
- Scrapes price information when available
- Prioritizes `Partineh` and falls back to `Asamkala` if not found
- Outputs human-readable results to the console and a file
- Headless Chrome browser for silent execution

---

## 📦 Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (must match your Chrome version)

Install dependencies using `pip`:

```bash
pip install selenium
```
---
## 🔧 Setup
Make sure Google Chrome is installed.

Download the correct version of ChromeDriver and make sure it’s in your system PATH.

Clone this repository or copy the script.

Add or update the list of item codes in the items list inside the script if needed.

## 🖥️ Usage
Run the script:

bash
Copy
Edit
python your_script_name.py
This will:

Search for each item on Partineh

If not found, try Asamkala

Print results to the console

Save all results in result.txt
---
## 📄 Output Format
Each line in the output looks like:

```
SY2000-0R4G-S2: 1,230,000 تومان (Found on Partineh)
SY2000-0R7G-S2: ❌ Not found on Partineh or Asamkala
```
---
## 📁 Output File
A file named result.txt will be created in the same directory, containing the final results.
---
## 🛑 Notes
This script runs in headless mode (no browser window pops up).

Page structure of Partineh or Asamkala may change, which could break the scraper.

Some items may take a few seconds due to network delays.

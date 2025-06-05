from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

items = [
    "SY2000-0R4G-S2",
    "SY2000-0R7G-S2",
    "SY2000-1R5G-S2",
    "SY2000-2R2G-S2",
    "SY2000-1R5G-4",
    "SY2000-2R2G-4",
    "SY2000-4G-S2",
    "SY2000-004G-4",
    "SY2000-5R5G-4",
    "SY2000-7R5G-4",
    "SY5000-0R7G-S2",
    "SY5000-1R5G-S2",
    "SY5000-2R2G-S2",
    "SY5000-0R7G-4",
    "SY5000-1R5G-4",
    "SY5000-2R2G-4",
    "SY5000-004G/4R5P-4",
    "SY5000-5R5G/7R5P-4",
    "SY5000-7R5G/11P-4",
    "SY5000-11G/15P-4",
    "SY5000-15G/18P-4",
    "SY5000-18G/22P-4",
]

for item in items:
    url = f"https://partineh.com/search?q={item}&instock=1"
    driver.get(url)

    try:
        price_elem = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "price-place-show"))
        )
        price = driver.execute_script("return arguments[0].innerText", price_elem).strip()

        if not price:
            if "محصولی یافت نشد" in driver.page_source:
                price = "Product not found"
            else:
                price = "No price listed"

    except:
        price = "Not found"

    print(f"{item}: {price}")

driver.quit()

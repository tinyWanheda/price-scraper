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
    "SJR2-3015",
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
    "SY5000-004G/5R5P-4",
    "SY5000-004G-S2",
    "SY5000-5R5G/7R5P-4",
    "SY5000-7R5G/11P-4",
    "SY5000-11G/15P-4",
    "SY5000-15G/18P-4",
    "SY5000-18G/22P-4",

]

results = []

for item in items:
    found = False
    price = ""
    source = ""

    # Try partineh.com first
    url_partineh = f"https://partineh.com/search?q={item}&instock=1"
    driver.get(url_partineh)

    try:
        price_elem = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "price-place-show"))
        )
        price = driver.execute_script("return arguments[0].innerText", price_elem).strip()
        if price:
            found = True
            source = "Partineh"
    except:
        pass

    # If not found on partineh.com, try asamkala.com
    if not found:
        url_asamkala = f"https://asamkala.com/Search?q={item}"
        driver.get(url_asamkala)

        try:
            price_elem = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "amount"))
            )
            price = driver.execute_script("return arguments[0].innerText", price_elem).strip()
            if price:
                found = True
                source = "Asamkala"
        except:
            pass

    # Prepare result string
    if found:
        result_line = f"{item}: {price} (Found on {source})"
    else:
        result_line = f"{item}: ❌ Not found on Partineh or Asamkala"

    print(result_line)
    results.append(result_line)

# Save to a text file
with open("results.txt", "w", encoding="utf-8") as file:
    for line in results:
        file.write(line + "\n")

driver.quit()

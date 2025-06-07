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
    "SY5000-004G/5R5P-4",
    "SY5000-004G-S2",
    "SY5000-5R5G/7R5P-4",
    "SY5000-7R5G/11P-4",
    "SY5000-11G/15P-4",
    "SY5000-15G/18P-4",
    "SY5000-18G/22P-4",
    "SY-130SP200A20TAYYB/SY200-200A-2(00)",
    "SY-130SP200A20TBYYB/SY200-200A-2(00)",
    "SY-180SP300A15TAYYD/SY200-300A-4(00)",
    "SY-180SP300A15TBYYD/SY200-300A-4(00)",
    "SY-180SP450A15TAYYD/SY200-450A-4(00)",
    "SY-180SP450A15TBYYD/SY200-450A-4(00)",
    "SY-180SP550A15DAYYD/SY200-550A-4(00)",
    "SY-180SP750A15DAYYD/SY200-750A-4(00)",
    "SJR2-3015",
    "SJR2-3018",
    "SJR2-3022",
    "SJR2-3030",
    "SJR2-3037",
    "SJR3-5075",
    "SJR2-3045/SJR3-5045",
    "SJR2-3055/SJR3-5055",
    "SJR2-3090/SJR3-5090",
    "SJR2-3110/SJR3-5110",
    "SJR2-3132/SJR3-5132",
    "SJR2-3160/SJR3-5160",
    "SJR2-3250/SJR3-5250",
    "SJR2-3200/SJR3-5200",
    "SY2000-0R7G-4",
    "SY5000-18G/22P-4",
    "SY5000-30G/37P-4",
    "SY5000-22G/30P-4",
    "SY5000-37G/45P-5",
    "SY9000-1R5G-4",
    "SY9000-2R2G-4",
    "SY9000-4G/5R5P-4",
    "SY9000-30G/37P",
    "SY9000-5R5G/7R5P-4",
    "SY9000-7R5G/11P-4",
    "SY9000-11G/15P-4",
    "SY9000-15G/18P-4",
    "SY9000-22G/30P-4",
    "SY9000-45G/55P-4",
    "SY9000-55G/75P-4",
    "SY9000-18G/22P-4",
    "SY9000-37G/45P-4",
    "SY8600-1R5G-4",
    "SY8600-2R2G-4",
    "SY8600-0R7G-4",
    "SY8600-4G/5R5P-4",
    "SY8600-5R5G/7R5P-4",
    "SY8600-7R5G/11P-4",
    "SY8600-011G/15P-4",
    "SY8600-15G/18P-4",
    "SY8600-18G/22P-4",
    "SY8600-22G/30P-4",
    "SY8600-30G/37P-4",
    "SY8600-37G/45P-4",
    "SY8600-75G-4/90P-4",
    "SY8600-90G/110P-4",
    "SY8600-110G/132P-4",
    "SY8600-132G/160P-4",
    "SY8600-160G/185P-4",
    "SY8600-45G/55P-4",
    "SY8600-55G/75P-4",
    "SY-80KP75A30BAYYB/SY200-75A-2(00)",
    "SY-130SP150A20SAYYB/SY200-150A-2(00)",
    "SY-130SP150A20SBYYB/SY200-150A-2(00)",
    "SY-130SP200A20SAYYB",
    "SY-180SP300A15SAYYD/SY200-300A-4(00)",
    "SY-180SP430A15SAYYD/SY200-450A-4(00)",
    "SY-180SP430A15SBYYD/SY200-450A-4(00)",
    "SY-180SP550A15SAYYD/SY200-550A-4(00)",
    "SY-180SP550A15SBYYD/SY200-550A-4(00)",
    "SY-180SP750A15SAYYD/SY200-750A-4(00)",
    "SY-180SP750A15SBYYD/SY200-750A-4(00)",
    "SY5000-4G-S2/SY200-100A-2",
    "SY-130SP150A20TAYYB/SY200-150A-2(00)",
    "SY-130SP150A20TBYYB/SY200-150A-2(00)"
]


results = []

for item in items:
    found = False
    price = ""
    source = ""

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

    if found:
        result_line = f"{item}: {price} (Found on {source})"
    else:
        result_line = f"{item}: ❌ Not found on Partineh or Asamkala"

    print(result_line)
    results.append(result_line)

with open("result.txt", "w", encoding="utf-8") as file:
    for line in results:
        file.write(line + "\n")

driver.quit()
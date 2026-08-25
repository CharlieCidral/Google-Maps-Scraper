from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv
import logging

# Configurar logging
logging.basicConfig(filename='process_log_ctba.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Record the start time
start_time = time.time()

# Setup webdriver
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# Open the webpage
# joinville
# driver.get('https://www.google.com.br/maps/search/quadras+joinville/@-26.3055352,-48.8381984,11z/data=!3m1!4b1?entry=ttu')
# são josé dos pinhais
# driver.get('https://www.google.com.br/maps/search/S%C3%A3o+Jos%C3%A9+dos+Pinhais+quadras/@-25.5391644,-49.2108185,13z/data=!3m1!4b1?entry=ttu')
# curitiba
driver.get('https://www.google.com.br/maps/search/curitiba+quadras/@-25.4621,-49.3124653,11z/data=!3m1!4b1?entry=ttu')
logging.info("Page opened")

# Wait for the page to load completely
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="feed"]')))
logging.info("Page loaded")

# Find the div with role="feed"
feed = driver.find_element(By.XPATH, '//div[@role="feed"]')

# Initial scroll
driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", feed)
logging.info("Initial scroll done")

# Wait for the new content to load
time.sleep(5)

# Now you can parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find the div with class "TFQHme"
target_divs = soup.find_all("div", class_="TFQHme")
logging.info(f"Found {len(target_divs)} target divs initially")

# Define the target quantity
target_quantity = 100

# Initialize variable to store the previous length of target_divs
previous_len = 0

# Scroll until you have the desired quantity or no more new divs are found
while len(target_divs) < target_quantity and len(target_divs) != previous_len:
    # Store the current length of target_divs
    previous_len = len(target_divs)

    # Scroll the feed
    driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", feed)
    logging.info(f"Scrolling... Current number of divs: {len(target_divs)}")

    # Wait for the new content to load
    time.sleep(5)

    # Update the page source and find the target divs
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    target_divs = soup.find_all("div", class_="TFQHme")
    logging.info(f"Found {len(target_divs)} target divs after scrolling")

companies = []

for i, target_div in enumerate(target_divs):
    try:
        logging.info(f"Processing target div {i+1}/{len(target_divs)}")
        
        # Scroll every 3 items
        if i > 0 and i % 2 == 0:
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", feed)
            logging.info(f"Scrolled down after processing {i} items")
            time.sleep(10)

        # Find the previous sibling div to click on
        previous_div = target_div.find_previous_sibling("div")
        if previous_div:
            logging.info(f"i é: {i}")
            # Using XPath to find the corresponding element in Selenium
            j = 3 + 2*i
            logging.info(f"j é: {j}")
            xpath = f"//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{j}]"
            previous_div_element = driver.find_element(By.XPATH, xpath)
            logging.info(f"Previous div element: {previous_div_element}")
            previous_div_element.click()
            logging.info(f"Clicked on div {i+1}")

            # Wait for the modal to load
            time.sleep(5)

            # Parse the modal HTML with BeautifulSoup
            modal_soup = BeautifulSoup(driver.page_source, 'html.parser')

            # Find the first div with class "Io6YTe" inside the modal
            address_div = modal_soup.find("div", class_="Io6YTe")
            address = address_div.text if address_div else ''

            company_element = previous_div.find("div", class_="fontHeadlineSmall")
            company = company_element.text if company_element else ''

            phone_element = previous_div.find("span", class_="UsdlK")
            phone = phone_element.text if phone_element else ''

            website_element = modal_soup.find("a", {"data-value": "Website"})
            website = website_element["href"] if website_element else ''

            description_btn = modal_soup.select_one("div.LBgpqf > div > div:nth-child(2) > span:nth-child(1) > span > button")
            description = description_btn.text if description_btn else ''

            reviews_span = modal_soup.select_one("div.F7nice > span:nth-child(2) > span > span")
            num_reviews = reviews_span.text if reviews_span else ''

            rate_reviews_span = modal_soup.select_one("div.F7nice > span:nth-child(1) > span:nth-child(1)")
            rate_reviews = rate_reviews_span.text if rate_reviews_span else ''

            plus_code_btn = modal_soup.find("button", attrs={"data-tooltip": "Copiar Plus Code"}).find("div").find("div", class_="rogA2c").find("div", class_="Io6YTe fontBodyMedium kR99db")
            plus_code = plus_code_btn.text if plus_code_btn else ''

            img_cover_div = modal_soup.select_one("div.RZ66Rb.FgCUCc > button > img")
            img_url = img_cover_div["src"] if img_cover_div else ''

            # availability (fazer função de clique e extrair por dia da semana)
            # xpath_availability = f"//*[@id='QA0Szd']/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[9]/div[4]"
            # availability_div_element = driver.find_element(By.XPATH, xpath_availability)
            # logging.info(f"Previous div element: {availability_div_element}")
            # availability_div_element.click()
            # logging.info(f"Clicked on subdiv of div {i+1}")
            # time.sleep(2)

            # if availability_div_element:
            #     # Talvez precise recarregar o bs
            #     linhas = modal_soup.find_all("tr")
            #     availability = []
            #     for linha in linhas:
            #         celulas = linha.find_all('td')
            #         if len(celulas) >= 2:
            #             dia_semana = celulas[0].text.strip()
            #             horario = celulas[1].text.strip()
            #             av = f"{dia_semana}, {horario}"
            #             availability.append(av)

            accessibility_span = modal_soup.select_one("span.wmQCje.google-symbols")
            accessibility = 'true' if accessibility_span else 'false'

            if company:
                companies.append({
                    'Company': company,
                    'Description': description,
                    'Phone': phone,
                    'Address': address,
                    'Website': website,
                    'Total reviews': num_reviews,
                    'Rate reviews': rate_reviews,
                    'Plus code': plus_code,
                    'Image url': img_url,
                    'Accessibility': accessibility
                    # 'Availability': availability
                })
                logging.info(f"Added company: {company}")
            else:
                logging.warning(f"Company name not found in div {i+1}")

            time.sleep(2)

    except Exception as e:
        logging.error(f"Error processing target div {i+1}/{len(target_divs)}: {e}")
        driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", feed)
        logging.info(f"Scrolled down after error on item {i+1}")
        time.sleep(5)
        continue

# Don't forget to close the driver
driver.quit()
logging.info("Driver closed")

def save_to_csv(companies, filename='companies_data_ctba.csv'):
    keys = companies[0].keys() if companies else []  # Assuming jobs is not empty
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(companies)
    logging.info(f"Data saved to {filename}")

save_to_csv(companies)

# Record the end time
end_time = time.time()

# Calculate and print the elapsed time
elapsed_time = end_time - start_time
logging.info(f"The code took {elapsed_time/60:.2f} minutes to run.")

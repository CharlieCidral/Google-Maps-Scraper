---

# 🗺️ Google Maps Scraper

This project performs **web scraping on Google Maps** to collect detailed information about points of interest. Although the example is configured to search for **sports courts in Curitiba**, the same code can easily be adapted for different types of searches, such as **businesses, restaurants, gyms, schools**, and much more.

### 🚀 Features
- Automated location search on Google Maps.
- Extraction of information such as:
- Business/location name
- Address
- Phone number
- Website
- Description
- Reviews and ratings
- Plus Code
- Cover image URL
- Accessibility
- Pagination and automatic scrolling to collect multiple results.
- Data saving to a **CSV** file (`"companies_data_ctba.csv"`).
- Detailed process logging to a **log** file (`"process_log_ctba.log"`).

### 🛠️ Technologies used
- `"Python 3"`
- `"Selenium WebDriver"` (with ChromeDriver Manager)
- `"BeautifulSoup4"`
- `"CSV"`
- `"Logging"`

### 📂 Project structure
- `"driver.get()"`: Sets the Google Maps search URL (can be changed to any city or location type).
- `"scroll"`: Automatic scrolling to load more results.
- `"collect"`: Data extraction for each location.
- `"save_to_csv()"`: Exports collected data to a CSV file.
- `"logging"`: Logs each step of the process and any potential errors. ### ⚙️ How to run
1. Clone this repository:
```bash
git clone https://github.com/seuusuario/google-maps-scraper.git
```
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
*(Make sure to include `"selenium"`, `"beautifulsoup4"`, and `"webdriver-manager"` in `requirements.txt`.)*
3. Adjust the search URL in the code to match what you want to scrape:
```python
driver.get('https://www.google.com.br/maps/search/curitiba+quadras/')
```
Examples of other searches:
- `"https://www.google.com.br/maps/search/restaurantes+curitiba/"`
- `"https://www.google.com.br/maps/search/empresas+joinville/"`
- `"https://www.google.com.br/maps/search/academias+são+josé+dos+pinhais/"`
4. Run the script:
```bash
python main.py
```
5. The results will be saved to `"companies_data_ctba.csv"`. ### 📊 Output example
```csv
"Company","Description","Phone","Address","Website","Total reviews","Rate reviews","Plus code","Image url","Accessibility"
"Quadra Esportiva X","","(41) 99999-9999","Rua das Flores, Curitiba","www.quadraX.com","120","4.5","J9P2+X5 Curitiba","https://maps.gstatic.com/...","true"
"Academia Y","Weight training and sports","(41) 98888-8888","Av. Brasil, Curitiba","","85","4.2","J9P3+Y6 Curitiba","","false"
```

### ⚠️ Notes
- Google Maps may change its HTML structure, which could require code adjustments.
- Excessive scraping may lead to temporary blocks. It is recommended to add **delays** or use **IP rotation** techniques to avoid restrictions.
- This project is for educational and learning purposes only.

---

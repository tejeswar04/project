import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Define a custom expected condition to wait for the overlay to disappear
def wait_for_overlay_to_disappear(driver):
    try:
        overlay = driver.find_element(By.ID, "overlay-loading")
        return "display: none" in overlay.get_attribute("style")
    except:
        return True

# Topics and countries to iterate over
topics = [
    "ai", "vision", "mlmining", "nlp", "inforet",
    "bed", "comm", "ops", "mod", "soft",
    "crypt", "chi", "robotics", "graph", "bio"
]
# topics=["robotics"]
countries = ["us", "ca", "uk", "au", "de"]

# Output CSV file
output_file = "cd.csv"

# Initialize the WebDriver

# Open the CSV file for writing
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Topic", "Country", "University Name", "Score"])

    # Iterate over topics and countries
    for topic in topics:
        for country in countries:
            driver = webdriver.Chrome()
            url = f"https://csrankings.org/#/fromyear/2020/toyear/2024/index?{topic}&{country}"
            driver.get(url)
            driver.execute_script(f"window.location.href = '{url}';")
            # Wait for the overlay to disappear
            WebDriverWait(driver, 30).until(wait_for_overlay_to_disappear)
            # time.sleep(1)  # Additional buffer time for loading

            # Get the page source and parse it with BeautifulSoup
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, "html.parser")
            ranking_table = soup.find("table", id="ranking")

            # Extract data from the table
            if ranking_table:
                tbody = ranking_table.find("tbody")
                if tbody:
                    rows = tbody.find_all("tr")
                    for row in rows:
                        columns = row.find_all("td")
                        if len(columns) == 4:
                            spans = columns[1].find_all("span")
                            separated_values = [span.get_text().strip() for span in spans]
                            if separated_values[0] == "►":  # Arrow symbol (►)
                                university_name = separated_values[1]
                                score = columns[2].get_text(strip=True) if len(columns) > 2 else None
                                if university_name and score:
                                    print(f'univ name : {university_name} score : {score}')
                                    csvwriter.writerow([topic, country, university_name, score])
            
            print(f"Data collected for Topic: {topic}, Country: {country}")

# Close the WebDriver
            driver.quit()

print("Data scraping completed and saved to csrankings_data.csv.")



import pandas as pd
from duckduckgo_search import DDGS

# Replace these with your actual API key and CX from Google Custom Search


# Load the CSV file into a DataFrame
filtered_data = pd.read_csv('cleaned_file.csv')

# Check if the 'name' column exists and get unique university names
if 'name' in filtered_data.columns:
    unique_univ_names = filtered_data['name'].unique()[170:]  # Get first 100 unique university names
    print(f"Found {len(unique_univ_names)} unique universities.")
else:
    print("The column 'name' does not exist in the CSV.")
    unique_univ_names = []
print(len(unique_univ_names))
print(unique_univ_names[0])
# Create an empty list to store results
result_data = []

# Define the API query function
def get_logo_url(univ_name):
    query = f"{univ_name} logo"
    results = DDGS().images(
        keywords=query,
        region="wt-wt",
        safesearch="off",
        size=None,
        color="Monochrome",
        type_image=None,
        layout=None,
        license_image=None,
        max_results=1,
    )
    if(len(results)>0):
        return (results[0]['image'])
    else:
        print(univ_name)
        return None

# Iterate over the first 100 universities and get the logo URLs
for univ_name in unique_univ_names:
    logo_url = get_logo_url(univ_name)
    result_data.append({'name': univ_name, 'image_url': logo_url})

# Create a DataFrame from the results
result_df = pd.DataFrame(result_data)

# Save the results to a new CSV file
result_df.to_csv('universities_with_logo_urls3.csv', index=False)

print("CSV file with university logos saved as 'universities_with_logo_urls.csv'.")
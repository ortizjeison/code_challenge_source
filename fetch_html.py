from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def fetch_html():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Fetch the website
    url = "https://www.yogonet.com/international/"
    driver.get(url)

    # Get the page source (HTML)
    html = driver.page_source

    # Save the HTML to a file
    with open("tmp/website.html", "w", encoding="utf-8") as file:
        file.write(html)

    # Close the WebDriver
    driver.quit()
    return html

if __name__ == "__main__":
    fetch_html()
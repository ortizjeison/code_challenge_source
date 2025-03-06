from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


local = False

def fetch_html():
    """
    Fetches the HTML content of a specified website using a headless Chrome browser.
    This function sets up Chrome options for headless browsing, initializes the WebDriver,
    navigates to the specified URL, retrieves the page source (HTML), saves it to a file,
    and then closes the WebDriver.
    Returns:
        str: The HTML content of the fetched website.
    """
    # Set up Chrome options
    chrome_options = Options()

    if local:
        pass
    else:
        chrome_options.binary_location = "/opt/google/chrome/chrome" # specify the path to the Chrome binary
    
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
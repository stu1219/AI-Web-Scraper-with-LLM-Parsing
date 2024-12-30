from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.remote.remote_connection import RemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get WebDriver URL with fallback
SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER", "http://localhost:4444/wd/hub")

if not SBR_WEBDRIVER:
    raise ValueError("SBR_WEBDRIVER environment variable is not set or invalid!")

print("SBR_WEBDRIVER:", SBR_WEBDRIVER)

def scrape_website(website):
    print("Connecting to Scraping Browser...")

    # Establish remote connection
    sbr_connection = RemoteConnection(SBR_WEBDRIVER, keep_alive=True)

    # Configure Chrome options
    options = ChromeOptions()
    options.add_argument("--headless")  # Optional: headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    with Remote(sbr_connection, options=options) as driver:
        driver.get(website)

        # Debug progress
        print("Scraping website:", website)

        # Handle CAPTCHA (Optional, depending on your setup)
        try:
            print("Waiting captcha to solve...")
            solve_res = driver.execute(
                "executeCdpCommand",
                {
                    "cmd": "Captcha.waitForSolve",
                    "params": {"detectTimeout": 10000},
                },
            )
            print("Captcha solve status:", solve_res["value"]["status"])
        except Exception as e:
            print("CAPTCHA handling skipped or not required.", e)

        # Scrape HTML content
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    # Remove script and style tags
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Clean and format text
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]

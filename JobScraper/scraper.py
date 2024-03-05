import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup

async def fetch_job_urls():
    browser = await launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto('https://hitmarker.net/jobs?keyword=data', waitUntil='networkidle0')
    
    # Scroll to the bottom of the page to ensure all dynamic content is loaded
    await page.evaluate('window.scrollTo(0, document.body.scrollHeight);')
    
    # Wait for the page to load and for JavaScript to execute
    await asyncio.sleep(5)
    
    # Get the page content after JavaScript has likely loaded
    html_content = await page.content()
    await browser.close()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    a_tags = soup.find_all('a', href=True)
    filtered_tags = [tag for tag in a_tags if "https://hitmarker.net/jobs/" in tag['href']]
    
    job_urls = [tag['href'] for tag in filtered_tags]
    return job_urls

# Since pyppeteer is async, we need to run the function in an event loop
if __name__ == "__main__":
    urls = asyncio.get_event_loop().run_until_complete(fetch_job_urls())
    print(urls)

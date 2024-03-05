import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def fetch_job_urls():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://hitmarker.net/jobs?keyword=data', wait_until='networkidle')

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

# Since this is an async function, we run it in an event loop
if __name__ == "__main__":
    urls = asyncio.run(fetch_job_urls())
    print(urls)

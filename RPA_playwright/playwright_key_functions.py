from playwright.async_api import async_playwright
import asyncio


async def playwright_function():
    async with async_playwright() as k:   # k means opeartion (any name will assign for operations)
        browser = await k.chromium.launch(headless=False)
        pages = await browser.new_page()

        #navigation
        await pages.goto("https://edge.com")

        await pages.wait_for_timeout(100000)
        await browser.close()

        #css selector, xpath

if __name__ == "_main_":
    asyncio.run(playwright_function())





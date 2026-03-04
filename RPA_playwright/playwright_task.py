from playwright.sync_api import sync_playwright

SEARCH_QUERY = "AI and AI agent difference"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            user_data_dir="C:/playwright_profile",  # Creates real browser profile
            headless=False,
            args=["--start-maximized"]
        )

        page = browser.new_page()

        print("Opening Bing...")
        page.goto("https://www.bing.com")

        # Wait manually first time if CAPTCHA appears
        page.wait_for_timeout(5000)

        search_box = page.locator("#sb_form_q")
        search_box.fill(SEARCH_QUERY)
        search_box.press("Enter")

        page.wait_for_selector("li.b_algo")

        print("\nResults loaded successfully!")

        results = page.locator("li.b_algo h2").all_inner_texts()

        for i, title in enumerate(results[:5], start=1):
            print(f"{i}. {title}")

        page.wait_for_timeout(10000)
        browser.close()

run()
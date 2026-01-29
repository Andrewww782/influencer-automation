from playwright.sync_api import sync_playwright
import pandas as pd


def scrape_profiles():
    data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://books.toscrape.com/", timeout=60000)

        books = page.locator(".product_pod")
        count = books.count()

        for i in range(count):
            title = books.nth(i).locator("h3 a").get_attribute("title")
            link = books.nth(i).locator("h3 a").get_attribute("href")
            price = books.nth(i).locator(".price_color").inner_text()
            availability = books.nth(i).locator(".availability").inner_text().strip()

            data.append({
                "name": title,
                "profile_url": f"https://books.toscrape.com/{link}",
                "price": price,
                "availability": availability,
                "status": "Not Contacted"
            })

        browser.close()

    df = pd.DataFrame(data)
    df.to_csv("data/influencers.csv", index=False)
    print("✅ Profiles saved to data/influencers.csv")


if __name__ == "__main__":
    scrape_profiles()

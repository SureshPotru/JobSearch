from playwright.sync_api import sync_playwright

def fetch_linkedin_jobs():
    jobs = []

    url = (
        "https://www.linkedin.com/jobs/search/"
        "?keywords=DevOps%20AWS%20Kubernetes"
        "&location=Hyderabad"
    )

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_timeout(5000)

        cards = page.query_selector_all(".job-search-card")
        for c in cards[:10]:
            title = c.query_selector("h3").inner_text()
            company = c.query_selector("h4").inner_text()
            link = c.query_selector("a").get_attribute("href")

            jobs.append({
                "title": title,
                "company": company,
                "location": "Hyderabad",
                "url": link,
                "description": title
            })

        browser.close()

    return jobs

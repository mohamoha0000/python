import requests
from bs4 import BeautifulSoup

# الكلمات المفتاحية للوظائف بالإنجليزية والفرنسية
keywords = [
    "jobs", "careers", "employment", "vacancies", "hiring", "recruitment", "work",
    "opportunities", "join-us", "apply",
    "emploi", "carrière", "offres-emploi", "postes-vacants", "recrutement",
    "travail", "opportunités", "candidatures", "rejoindre", "embauche"
]

# قائمة المواقع لفحصها
sites = [
    "http://ondima.ma/",
    "https://northwebmedia.com/",
    "https://www.americaneagle.com/",
    "https://yeswelcome.ma/",
    "https://devtitechnologie.com/",
    "https://dijinord.com/contact/",
    "https://map-concepts.com/",
    "https://devnetcorp.com/",
    "http://mobicentrum.com/",
    "https://www.tingisweb.com/",
    "https://onnvision.com/",
    "https://nostrum.ma/",
    "https://webessource.com/",
    "https://devoratech.com/",
    "https://www.growthmarketingsolutions.ma/"
]

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; JobLinkFinder/1.0; +https://yourdomain.com)"
}

def find_job_links(site):
    print(f"Checking site: {site}")
    try:
        resp = requests.get(site, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        links = soup.find_all("a", href=True)
        found_links = set()
        for link in links:
            href = link['href'].lower()
            for kw in keywords:
                if kw in href:
                    # طباعة الرابط بشكل كامل
                    if href.startswith("http"):
                        found_links.add(href)
                    else:
                        # بناء رابط كامل لو الرابط نسبي
                        from urllib.parse import urljoin
                        full_url = urljoin(site, href)
                        found_links.add(full_url)
                    break
        if found_links:
            print(f"Found job-related links on {site}:")
            for l in found_links:
                print("  -", l)
        else:
            print("No job-related links found.")
    except Exception as e:
        print(f"Error checking {site}: {e}")

if __name__ == "__main__":
    for s in sites:
        find_job_links(s)
        print("-" * 50)

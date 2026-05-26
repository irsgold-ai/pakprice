from scrapers.daraz import DarazScraper
from scrapers.priceoye import PriceOyeScraper
from scrapers.all_scrapers import TelemartScraper,SymbiosScraper,IShoppingScraper
SCRAPER_REGISTRY={"daraz":DarazScraper,"priceoye":PriceOyeScraper,"telemart":TelemartScraper,"symbios":SymbiosScraper,"ishopping":IShoppingScraper}
def get_scraper(site_key):
    cls=SCRAPER_REGISTRY.get(site_key)
        return cls() if cls else None
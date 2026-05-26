from bs4 import BeautifulSoup
import sys,os
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scrapers.base_scraper import BaseScraper
import config
class DarazScraper(BaseScraper):
    def __init__(self):super().__init__("daraz")
        def scrape(self,query):
                results=[]
                        html=self.fetch_page(self.build_search_url(query))
                                if not html:return results
                                        soup=BeautifulSoup(html,'html.parser')
                                                cards=soup.find_all('div',{'class':lambda x:x and 'gridItem' in x}) or soup.find_all('div',{'data-qa-locator':'product-item'}) or soup.find_all('div',{'class':lambda x:x and 'card' in str(x).lower()})
                                                        for card in cards[:config.MAX_RESULTS]:
                                                                    try:
                                                                                    name_tag=card.find('div',{'class':lambda x:x and 'title' in str(x).lower()}) or card.find('a',title=True) or card.find('h2') or card.find('h3')
                                                                                                    if not name_tag:continue
                                                                                                                    name=name_tag.get('title','') or name_tag.get_text(strip=True)
                                                                                                                                    if not name:continue
                                                                                                                                                    price_tag=card.find('span',{'class':lambda x:x and 'price' in str(x).lower()}) or card.find('div',{'class':lambda x:x and 'price' in str(x).lower()})
                                                                                                                                                                    price=self.clean_price(price_tag.get_text(strip=True)) if price_tag else 0
                                                                                                                                                                                    if price<=0:continue
                                                                                                                                                                                                    link=card.find('a',href=True)
                                                                                                                                                                                                                    url=""
                                                                                                                                                                                                                                    if link:
                                                                                                                                                                                                                                                        h=link.get('href','')
                                                                                                                                                                                                                                                                            url=h if h.startswith('http') else('https:'+h if h.startswith('//') else self.base_url+h)
                                                                                                                                                                                                                                                                                            img=card.find('img')
                                                                                                                                                                                                                                                                                                            image=(img.get('src','') or img.get('data-src','')) if img else ""
                                                                                                                                                                                                                                                                                                                            orig_tag=card.find('del')
                                                                                                                                                                                                                                                                                                                                            orig=self.clean_price(orig_tag.get_text(strip=True)) if orig_tag else 0
                                                                                                                                                                                                                                                                                                                                                            disc=f"{int(((orig-price)/orig)*100)}% OFF" if orig>price>0 else ""
                                                                                                                                                                                                                                                                                                                                                                            results.append(self.format_result(name,price,url,image,orig,disc))
                                                                                                                                                                                                                                                                                                                                                                                        except:continue
                                                                                                                                                                                                                                                                                                                                                                                                return results
SITES_TO_SCRAPE = ["daraz","priceoye","telemart","symbios","ishopping"]
PRICE_RANGE_BUFFER_PERCENT = 10
MAX_RESULTS = 20
MAX_ALTERNATIVES = 6
CACHE_MINUTES = 20
REQUEST_TIMEOUT = 15
DELAY_BETWEEN_REQUESTS = 1
MAX_RETRIES = 2
APP_NAME = "PakPrice"
APP_TAGLINE = "Pakistan's Smartest Price Comparison"
CURRENCY = "Rs."
APP_VERSION = "1.0.0"
DATABASE_PATH = "database/pakprice.db"
CATEGORIES = {"all":{"name":"All Categories","keywords":[],"icon":"🔍"},"mobiles":{"name":"Mobile Phones","keywords":["samsung","iphone","apple","xiaomi","oppo","vivo","realme","huawei","nokia","infinix","tecno","mobile","phone","smartphone"],"icon":"📱"},"laptops":{"name":"Laptops & Tablets","keywords":["laptop","notebook","tablet","ipad","dell","hp","lenovo","asus","acer","macbook"],"icon":"💻"},"appliances":{"name":"Home Appliances","keywords":["ac","refrigerator","fridge","washing machine","microwave","oven","television","tv","led","air conditioner","geyser","fan","blender"],"icon":"🏠"},"electronics":{"name":"Electronics","keywords":["headphones","earphones","speaker","camera","printer","router","keyboard","mouse","monitor","charger","power bank","cable","smartwatch"],"icon":"🔌"},"groceries":{"name":"Packaged Groceries","keywords":["nestle","unilever","tapal","lipton","surf","ariel","dettol","shampoo","oil","ghee","flour","rice","sugar","milk","juice"],"icon":"🛒"}}
SITE_INFO = {"daraz":{"name":"Daraz","base_url":"https://www.daraz.pk","search_url":"https://www.daraz.pk/catalog/?q=","logo":"🛍️","color":"#F57224","trustworthy":True},"priceoye":{"name":"PriceOye","base_url":"https://priceoye.pk","search_url":"https://priceoye.pk/search?q=","logo":"💰","color":"#E31837","trustworthy":True},"telemart":{"name":"Telemart","base_url":"https://www.telemart.pk","search_url":"https://www.telemart.pk/search?q=","logo":"📡","color":"#0066CC","trustworthy":True},"symbios":{"name":"Symbios","base_url":"https://symbios.pk","search_url":"https://symbios.pk/search?keyword=","logo":"⚡","color":"#FF6600","trustworthy":True},"ishopping":{"name":"iShopping","base_url":"https://www.ishopping.pk","search_url":"https://www.ishopping.pk/search?q=","logo":"🍎","color":"#555555","trustworthy":True}}
REQUEST_HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36","Accept-Language":"en-US,en;q=0.9","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
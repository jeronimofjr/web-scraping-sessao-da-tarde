from app.crawler import Scraping

def init():
    scraping = Scraping()
    scraping.scraping_data()
    scraping.processing()
    scraping.save_data()

if __name__ == "__main__":
    init()
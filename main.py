from scraping.scraping import Scraping

def init_scraping():
    scraping = Scraping()
    scraping.scraping_data()
    scraping.processing()
    scraping.save_data()

if __name__ == "__main__":
    init_scraping()
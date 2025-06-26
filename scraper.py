import requests
from bs4 import BeautifulSoup
import csv

URL = 'http://quotes.toscrape.com'
CSV_FILE = 'quotes.csv'

def scrape_quotes():
    page = 1
    all_quotes = []

    while True:
        res = requests.get(f"{URL}/page/{page}/")
        if res.status_code != 200:
            break

        soup = BeautifulSoup(res.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')

        if not quotes:
            break

        for quote in quotes:
            text = quote.find('span', class_='text').text.strip()
            author = quote.find('small', class_='author').text.strip()
            all_quotes.append([text, author])
        
        page += 1

    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Quote', 'Author'])
        writer.writerows(all_quotes)

    print(f"✅ {len(all_quotes)} quotes scraped and saved to {CSV_FILE}.")

if __name__ == '__main__':
    scrape_quotes()

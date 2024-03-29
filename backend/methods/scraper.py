import requests
from bs4 import BeautifulSoup
from datetime import date

def handle_scrape():
    today = date.today()

    base_url = "https://www.gocomics.com/garfield/"

    url_date = today.strftime("%Y/%m/%d")

    full_url = "%s%s" % (base_url, url_date)
    
    # Making a GET request
    r = requests.get(full_url)
    
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    # Extract the garfield crap
    element_desired = soup.findAll(attrs={"data-feature-type" : "comic"})

    if element_desired:
        output_url = element_desired[0].get('data-image')

    return output_url

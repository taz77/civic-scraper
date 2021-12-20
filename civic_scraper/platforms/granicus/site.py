from requests import Session
import feedparser
import pprint

def fetch_url(session, url, **kwargs):
    response = session.get(url, headers=headers)
    return response.text

def parse_rss(url):
    parsed_rss = feedparser.parse(url)
    pprint.pprint(parsed_rss)
    return parsed_rss

if __name__ == '__main__':
    session = Session()
    headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}

    url = 'https://brookhavencityga.iqm2.com/Services/RSS.aspx?Feed=Calendar'

    rss_text = fetch_url(session, url, **headers)
    parse_rss(url)


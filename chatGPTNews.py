import feedparser

def retrieve_rss_feed(url):
    d = feedparser.parse(url)
    return d.entries

# url = "https://www.finance.yahoo.com/rss/headline?s=AAPL"
bbc = "http://feeds.bbci.co.uk/news/world/rss.xml"
reuters = "http://feeds.marketwatch.com/marketwatch/topstories/"
# yahoo = "https://finance.yahoo.com/rss/topstories"
# motley = "https://www.fool.com/feeds/latest/all.xml"
entries = retrieve_rss_feed(reuters)

for entry in entries:
    print(entry.title)
    print(entry.link)
    print(entry.description)
    print("\n")

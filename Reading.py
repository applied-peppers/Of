def reading():
    from bs4 import BeautifulSoup
    import urllib.request
    raw_data = urllib.request.urlopen("https://www.youtube.com/feed/subscriptions")
    data=raw_data.read().decode('cp1251')
    print(data)
reading()
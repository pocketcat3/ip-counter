import bs4, requests, time
s = requests.get('https://2ip.ua/ru/')
b = bs4.BeautifulSoup(s.text, "html.parser")
a = b.select(" .ipblockgradient .ip")[0].getText()
print(a)
time.sleep(5)
import bs4, requests

def webSkrejper(url):
	res = requests.get(url)
	res.raise_for_status()

	supa = bs4.BeautifulSoup(res.text, 'html.parser')
	elementi = supa.select('css-elementi')
	return elementi[0].text.strip()

celta = webSkrejper('url')
print('Ja najdovme ' + celta)

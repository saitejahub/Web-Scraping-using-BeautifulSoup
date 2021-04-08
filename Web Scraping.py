import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.magicbricks.com/flats-in-hyderabad-for-sale-pppfs?mbtracker=google_paid_brand_desk_hyderabad&ccode=brand_sem&gclid=CjwKCAjw07qDBhBxEiwA6pPbHniLCfaw9koCTVEZb2AOFaGGS6SCBJW9iUtlDTulHeaub-5QTKBA0BoC67wQAvD_BwE")
soup=BeautifulSoup(response.content,"html.parser")
cards=soup.find_all("div",attrs={"class":"m-srp-card__container"})
for card in cards:
	title=card.find("span",attrs={"class":"m-srp-card__title__bhk"})
	price=card.find("div",attrs={"class":"m-srp-card__price"})
	area=card.find("div",attrs={"class":"m-srp-card__summary__info"})
	data="{} {} {}".format(title.text.strip("\n"),price.text,area.text)
	print(data)
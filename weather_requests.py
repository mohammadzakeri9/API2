#=============== moduls ===============
import requests
from bs4 import BeautifulSoup

# ------------------------------------- Requests ---------------------------------- 
#=============== Tehran ===============
url_tehran = requests.get("https://www.euronews.com/weather/asia/iran/tehran")
soup1 = BeautifulSoup(url_tehran.text, "html.parser")
tehran_weather = soup1.find("span", attrs={"class":"c-swiper-slide--day__temp-max unit_C"}).text

#=============== Ankara ===============
url_ankara = requests.get("https://www.euronews.com/weather/europe/turkey/ankara")
soup2 = BeautifulSoup(url_ankara.text, "html.parser")
ankara_weather = soup2.find("span", attrs={"class":"c-swiper-slide--day__temp-max unit_C"}).text

#=============== Washington ===============
url_washington = requests.get("https://www.euronews.com/weather/north-america/united-states/ar/washington")
soup3 = BeautifulSoup(url_washington.text, "html.parser")
washington_weather = soup3.find("span", attrs={"class":"c-swiper-slide--day__temp-max unit_C"}).text

#=============== Paris ===============
url_paris = requests.get("https://www.euronews.com/weather/europe/france/paris")
soup4 = BeautifulSoup(url_paris.text, "html.parser")
Paris_weather = soup4.find("span", attrs={"class":"c-swiper-slide--day__temp-max unit_C"})

#=============== Berlin ===============
url_berlin = requests.get("https://www.euronews.com/weather/europe/germany/berlin")
soup5 = BeautifulSoup(url_berlin.text, "html.parser")
Berlin_weather = soup5.find("span", attrs={"class":"c-swiper-slide--day__temp-max unit_C"})

#=============== Dubai ===============
url_dubai = requests.get("https://www.euronews.com/weather/asia/united-arab-emirates/dubai")
soup6 = BeautifulSoup(url_dubai.text, "html.parser")
Dubai_weather = soup6.find("span", attrs={"class":"c-swiper-slide--day__temp-max unit_C"})

#=============== Moscow ===============
url_moscow = requests.get("https://www.euronews.com/weather/europe/russia/moscow")
soup7 = BeautifulSoup(url_moscow.text, "html.parser")
Moscow_weather = soup7.find("span", attrs={"class":"c-swiper-slide--day__temp-max unit_C"})

#=============== Tokyo ===============
url_tokyo = requests.get("https://www.euronews.com/weather/asia/japan/tokyo")
soup8 = BeautifulSoup(url_tokyo.text, "html.parser")
Tokyo_weather = soup8.find("span", attrs={"class":"c-swiper-slide--day__temp-max unit_C"})

#=============== Ottawa ===============
url_ottawa = requests.get("https://www.euronews.com/weather/north-america/canada/ottawa")
soup9 = BeautifulSoup(url_ottawa.text, "html.parser")
Ottawa_weather = soup9.find("span", attrs={"class":"c-swiper-slide--day__temp-max unit_C"})

#=============== Islamabad ===============
url_islamabad = requests.get("https://www.euronews.com/weather/asia/pakistan/islamabad")
soup10 = BeautifulSoup(url_islamabad.text, "html.parser")
Islamabad_weather = soup10.find("span", attrs={"class":"c-swiper-slide--day__temp-max unit_C"})

# ------------------------------------- out put ----------------------------------
print("\n---------------------------------")
print(f"Tehran{tehran_weather}")
print("\n---------------------------------")
print(f"Ankara{ankara_weather}")
print("\n---------------------------------")
print(f"Washington{washington_weather}")
print("\n---------------------------------")
print(f"Paris{Paris_weather}")
print("\n---------------------------------")
print(f"Berlin{Berlin_weather}")
print("\n---------------------------------")
print(f"Dubai{Dubai_weather}")
print("\n---------------------------------")
print(f"Moscow{Moscow_weather}")
print("\n---------------------------------")
print(f"Tokyo{Tokyo_weather}")
print("\n---------------------------------")
print(f"Ottawa{Ottawa_weather}")
print("\n---------------------------------")
print(f"Islamabad{Islamabad_weather}")
print("\n---------------------------------")




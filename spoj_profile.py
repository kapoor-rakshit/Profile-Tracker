import bs4 as bs
import urllib.request

user = input("Enter username : ").strip()
url = "https://www.spoj.com/users/" + user

sitedata = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sitedata, 'html.parser')

details = soup.find(id="user-profile-left")
print(details.find("h3").text)
extra = details.find_all("p")
for i in extra:
	print(i.text)

print()
print(soup.find("dt").text, end=" : ")
print(soup.find("dd").text)
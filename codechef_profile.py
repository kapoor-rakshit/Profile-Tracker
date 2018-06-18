import requests
import bs4 as bs

user = input("Enter username : ").strip()
url = "https://www.codechef.com/users/" + user

resp = requests.get(url)
resp = resp.text

soup = bs.BeautifulSoup(resp, 'html.parser')

# to get the required tag select elem and inspect

details = soup.find(class_="user-details-container")
print("Name : ", details.find("h2").text)
extra = details.find(class_="user-details").find_all("li")
for i in extra:
	print(i.text)

print()
print("Current Rating : ", soup.find(class_="rating-number").text)
print(len(soup.find(class_="rating-star").find_all("span")), "Star(s)")

print()
print(soup.find(class_="rating-header").find("small").text)

print()
ranks = soup.find(class_="rating-ranks").find_all("a")
print("Global Rank : ", ranks[0].text)
print("Country Rank : ", ranks[1].text)

print()
table = soup.find(class_="rating-table")
headers = table.find_all("th")
tp=""
disp=[]
for h in headers:
	tp+=h.text + " | "
disp.append(tp)
content = table.find_all("td")
l = len(content)
for i in range(0,l,4):
	disp.append(content[i].text + " | " + content[i+1].text + " | " + content[i+2].text + " | " + content[i+3].text)

print(*disp,sep="\n")


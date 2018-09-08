import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
html = requests.get("http://www.doutula.com/article/list/",headers=headers)

soup = BeautifulSoup(html.text,"html.parser")

content = soup.select(".list-group-item")
for item in content:
    title = item.select(".random_title")[0].contents[0]
    pics = item.select("img")
    if title != "赞助商广告":
        print(title)
        for pic in pics:
            if pic.has_attr('data-original'):
                print(pic['data-original'])




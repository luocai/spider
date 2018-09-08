import requests
from bs4 import BeautifulSoup
import os
import urllib.request

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

html = requests.get("http://www.doutula.com/article/list/",headers=headers)

soup = BeautifulSoup(html.text,"html.parser")

href = soup.select(".list-group-item")

for item in href:
    if item.has_attr("href"):
        detail_url = item['href']

        html_detail = requests.get(detail_url, headers=headers)

        soup_detail = BeautifulSoup(html_detail.text, "html.parser")
        title = soup_detail.select(".pic-title h1 a")[0]
        pics = soup_detail.select(".artile_des img")

        print(title.text)
        dir = "D:/test/" + title.text
        if not os.path.exists(dir):
            os.makedirs(dir)
            print('文件夹创建成功')

        for pic in pics:
            url = pic['src']
            print(url)
            filename = url.split("/").pop()
            path = os.path.join(dir, filename)
            urllib.request.urlretrieve(url, filename=path)


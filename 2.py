import requests
from bs4 import BeautifulSoup
import os
import urllib.request

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
html = requests.get("https://www.doutula.com/article/detail/6411584",headers=headers)

soup = BeautifulSoup(html.text,"html.parser")

title = soup.select(".pic-title h1 a")[0]
pics = soup.select(".artile_des img")

print(title.text)
dir = "D:/test/" + title.text
if not os.path.exists(dir):
    os.makedirs(dir)
    print('文件夹创建成果')

for pic in pics:
    url = pic['src']
    print(url)
    filename = url.split("/").pop()
    path = os.path.join(dir,filename)
    urllib.request.urlretrieve(url,filename=path)


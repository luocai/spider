import requests
from bs4 import BeautifulSoup
import os
import urllib.request

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

BASE_URL = "https://www.doutula.com/article/list/?page="

def get_page(url):
    html = requests.get(url,headers=headers)
    return html.text

def get_detail_url(html):
    soup = BeautifulSoup(html, "html.parser")
    href = soup.select(".list-group-item")
    return href

def get_page_detail(html):
    soup_detail = BeautifulSoup(html, "html.parser")
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

def main():
    for i in range(1,5):
        page_url = BASE_URL + str(i)
        html = get_page(page_url)
        href = get_detail_url(html)
        for item in href:
            if item.has_attr("href"):
                detail_url = item['href']
                detail_html = get_page(detail_url)
                get_page_detail(detail_html)

if __name__ == "__main__":
    main()
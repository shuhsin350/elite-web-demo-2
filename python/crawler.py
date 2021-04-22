# 抓取網站原始碼
import urllib.request as req
url="https://www.dcard.tw/f/relationship"
#建立一個 Request 物件，附加  Request Headers 的資訊 (假裝是個正常使用者)
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# 解析原始碼，取得每篇文章標題
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("h2", class_="tgn9uw-2 jWUdzO") # 尋找文章標題 "class_="tgn9uw-2 jWUdzO" 的 h2標籤
for title in titles:
    if title.a != None:
        print(title.a.string)
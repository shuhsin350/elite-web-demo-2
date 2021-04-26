# 抓取網站原始碼  日經
import urllib.request as req
url="https://zh.cn.nikkei.com/"
#建立一個 Request 物件，附加  Request Headers 的資訊 (假裝是個正常使用者)
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# 解析原始碼，取得每篇文章標題
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("dt") 
for title in titles:
    if title.a != None:
        print(title.a.string)
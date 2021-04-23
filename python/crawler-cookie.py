# 抓取 PTT 八卦版 網站原始碼
import urllib.request as req
def getData(url): # 用函式做包裝
    #建立一個 Request 物件，附加  Request Headers 的資訊 (假裝是個正常使用者)       
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"
        
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # 解析原始碼，取得每篇文章標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title") # 尋找文章標題 "class_="title" 的 div標籤
    for title in titles:
        if title.a != None:
            print(title.a.string)
    # 抓取上一頁的連結
    nextLink=root.find("a",string="‹ 上頁")
    return nextLink["href"]
# 主程序 : 抓取一個頁面標題
pageUrl="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    pageUrl="https://www.ptt.cc"+getData(pageUrl)
    count+=1

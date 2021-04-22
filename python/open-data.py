# import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")
# print(data)

import urllib.request as request #載入模組，執行網路連線
import json #做json的資料解析
#資料整塊讀取下來
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response)
    
#解析資料
clist=data["result"] ["results"]
with open("data.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")
        # 檔案寫入公司名稱，加換行符號

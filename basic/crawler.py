#抓取PPT 電影版的網頁原始碼 (HTML)
import urllib.request as req
url="https://www.pttweb.cc/bbs/movie"
#建立一個request的物件
request = req.Request(url, headers={
    "User-Agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
print(data)
#urlopen有問題
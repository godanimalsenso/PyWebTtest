from WebPackage import GetContent

target_url = "https://24h.pchome.com.tw/store/DAAZ6A?style=2"
#取得網頁
soup = GetContent(target_url)

target_url = "https://24h.pchome.com.tw/prod/DAAK01-190092TVT"
#取得網頁
soup = GetContent(target_url)

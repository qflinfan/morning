import requests
import time

url = "https://api-mi.xsot.cn/user/checkin"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ4Y3NvZnQtbWktbWluaWFwcCIsImlhdCI6MTc2MzAwMDMyOCwiaWQiOjQzNywiZW1haWwiOiIiLCJyb2xlIjowfQ.vcHN9KLTaWUZ36PEilzwJMCb2DX_neM3_dOwLTiUI23pKwO0-eNrhMt-OdC4VWhQF2bUJdn_gGYGI7kRnyRSwA",
    "Content-Type": "application/json",
    "platform": "mp-weixin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf2541211) XWEB/16815"
}
data = {}  # 请求体

# 发送请求
response = requests.post(url, headers=headers, json=data)
print("签到结果：", response.text)

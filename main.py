import requests
import os
from datetime import datetime

def main():
    # 从环境变量获取配置
    auth_token = os.getenv("AUTH_TOKEN")
    checkin_url = os.getenv("CHECKIN_URL")

    # 校验必填参数
    if not auth_token or not checkin_url:
        print("❌ 配置错误：AUTH_TOKEN或CHECKIN_URL未设置")
        return

    # 构造请求头（完全复刻原请求，确保兼容性）
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
        "platform": "mp-weixin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf2541211) XWEB/16815",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Referer": "https://servicewechat.com/wxbd24984d48a60d92/16/page-frame.html",
        "SunnyNetHTTPClient": "true",
        "xweb_xhr": "1"
    }
    request_body = {}  # 请求体为空

    try:
        # 发送POST签到请求（超时10秒，避免卡壳）
        response = requests.post(
            url=checkin_url,
            headers=headers,
            json=request_body,
            timeout=10,
            verify=False  # 忽略SSL证书校验（部分环境可能需要）
        )
        # 打印详细日志（方便排查问题）
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"✅ 签到任务执行时间：{current_time}")
        print(f"✅ 响应状态码：{response.status_code}")
        print(f"✅ 响应结果：{response.text}")

        # 简单结果判断
        if response.status_code == 200:
            if "成功" in response.text or "已签到" in response.text:
                print("🎉 签到完成！")
            else:
                print("⚠️  签到结果异常，请查看响应内容")
        else:
            print(f"❌ 签到失败，状态码：{response.status_code}")

    except requests.exceptions.Timeout:
        print("❌ 签到超时，可能是网络问题或接口无响应")
    except requests.exceptions.ConnectionError:
        print("❌ 连接失败，可能是接口地址错误或网络不通")
    except Exception as e:
        print(f"❌ 签到异常：{str(e)}")

if __name__ == "__main__":
    main()

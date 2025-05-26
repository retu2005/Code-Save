import requests


def download_douyin_video(video_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.douyin.com/',
        'Origin': 'https://www.douyin.com',
    }

    # 需要手动设置有效的cookies
    cookies = {
        'ttwid': 'YOUR_TTWID_VALUE',
        'passport_csrf_token': 'YOUR_CSRF_TOKEN',
        'msToken': 'YOUR_MS_TOKEN'
    }

    try:
        session = requests.Session()
        response = session.get(video_url, headers=headers, cookies=cookies, stream=True)

        if response.status_code == 200:
            # 保存视频文件
            with open('douyin_video.mp4', 'wb') as f: # 替换为你想要的文件名
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            return "视频下载成功"
        return f"请求失败，状态码: {response.status_code}"
    except Exception as e:
        return f"发生错误: {str(e)}"


# 使用示例
video_url = input("请输入抖音视频链接: ")
result = download_douyin_video(video_url)
print(result)
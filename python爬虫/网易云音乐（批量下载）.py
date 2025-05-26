"""
仅限下载网页上可以听的音乐，不能下载付费音乐。
需要登陆
"""

# 用代码下载多个音乐
import requests
import re
import os

# 1.确定数据所在网址
url = 'https://music.163.com/discover/toplist?id=3778678'

# 2.伪装浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    'Referer': 'https://music.163.com/'
}

# 3.发送请求获取页面内容
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'  # 确保正确编码
html = response.text

# 4.解析数据
# 使用正则表达式匹配歌曲信息（注意：网页结构可能变化，需要定期更新正则）
pattern = r'<li><a href="/song\?id=(\d+)">(.*?)</a></li>'
song_list = re.findall(pattern, html)

# 创建保存目录
save_dir = '网易云音乐'
os.makedirs(save_dir, exist_ok=True)

# 5.下载歌曲
for song_id, song_name in song_list:
    # 清理文件名中的非法字符
    song_name = re.sub(r'[\\/:*?"<>|]', '', song_name)
    
    # 构造下载链接
    download_url = f'http://music.163.com/song/media/outer/url?id={song_id}.mp3'
    
    try:
        # 带headers请求，防止被拦截
        music_data = requests.get(download_url, headers=headers).content
        
        # 保存文件
        with open(f'{save_dir}/{song_name}.mp3', 'wb') as f:
            f.write(music_data)
        print(f'下载成功: {song_name}')
    except Exception as e:
        print(f'下载失败【{song_name}】: {str(e)}')

print('全部下载任务完成！')



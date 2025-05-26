import requests

url = input("请输入小破站视频url：")

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36','referer': 'https://www.bilibili.com/bangumi/play/ss45969?spm_id_from=333.337.0.0','origin': 'https://www.bilibili.com'}

cookies = {'SESSDATA':'568d907d%2C1761802365%2Cafe79%2A51CjBWYe__rMK8iwwPAjzoxCsS8bkM9C_TFhAn3XPITilzvBDqh3ZXpyD4Qo3P8sgKUxESVmpHeko5dk9DbDNnWGd2LU9XWFFrak9jWFR2VUxlRk1mWUxlNUZHSm5SNDllbm9uWmVJcktZS2VyYmR6aW1EanBNMXBjX2NnUVVhQXZwWkFyUHA0XzBBIIEC',
        'bili_jct':'3cfc1506bcc13ee33d64c32521ca6d7a',
        'buvid3':'B10E90BA-02B9-5592-E054-9D324A361C2523464infoc'}

res = requests.get(url, headers=headers, cookies=cookies)

open("视频.mp4", "wb").write(res.content)

music = input("请输入小破站音乐url：")

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36','referer': 'https://www.bilibili.com/bangumi/play/ss45969?spm_id_from=333.337.0.0','origin': 'https://www.bilibili.com'}

cookies = {'SESSDATA':'568d907d%2C1761802365%2Cafe79%2A51CjBWYe__rMK8iwwPAjzoxCsS8bkM9C_TFhAn3XPITilzvBDqh3ZXpyD4Qo3P8sgKUxESVmpHeko5dk9DbDNnWGd2LU9XWFFrak9jWFR2VUxlRk1mWUxlNUZHSm5SNDllbm9uWmVJcktZS2VyYmR6aW1EanBNMXBjX2NnUVVhQXZwWkFyUHA0XzBBIIEC',
        'bili_jct':'3cfc1506bcc13ee33d64c32521ca6d7a',
        'buvid3':'B10E90BA-02B9-5592-E054-9D324A361C2523464infoc'}

res = requests.get(music, headers=headers, cookies=cookies)

open("音频.mp3", "wb").write(res.content)





from moviepy import AudioFileClip, VideoFileClip

audio = AudioFileClip("音频.mp3")

vidio = VideoFileClip("视频.mp4")

vidio_with_audio = vidio.with_audio(audio)

vidio_with_audio.write_videofile("完整视频_5.mp4")

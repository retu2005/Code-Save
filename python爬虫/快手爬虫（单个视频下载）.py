"""
快手视频单个下载
"""

#下载快手无水印视频
import requests
#1.确定数据所在网址  变量赋值  变量  容器
url = input('请输入视频地址:')
#2.对目标网站发出请求  获取视频的二进制数据  get  post
#矿泉水 = 手机.付款(2)
#状态码 200 成功  302 301 404 500  请求失败
#.text  获取字符串数据  .content获取二进制数据    .json()获取json数据/字典
res = requests.get(url).content
#3.将数据保存到本地
#w 写入文本数据   wb 写入二进制数据    a 追加写入   rb 追加写入二进制数据
open('kuaishou_video.mp4','wb').write(res)


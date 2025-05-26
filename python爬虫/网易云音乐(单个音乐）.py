"""
仅限下载网页上可以听的音乐，不能下载付费音乐。
需要登陆
"""


import requests#导入数据请求模块  第三方工具包  需要安装
#命令：pip install requests
#win+R  输入cmd  输入安装命令：pip install requests
#一.用代码下载单个音乐
#1.确定数据所在网址  变量赋值  变量  容器  储存数据
url = 'https://m704.music.126.net/20250421094806/ec9b93e7fa66bf568fbf5ee12b003a56/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/14096439245/62a1/06a8/2190/add9ea0368d8363d47739aae6d836de5.m4a?vuutv=ULjY2P/s8STuLfB/mYcCDG7BRrCcQ67bd8IofTQ+MzyL7J+Ur+qli9fDmyR86V20p2URRiMrDzKKFS3KRTbummHtVFwYJC3OoKj1srmn7s4=&authSecret=0000019655f11bc61d980a6490900006'
#2.对目标网址发送请求  获取响应的音乐的二进制数据  请求方式：get()  post()
#美照 = 手机.拍照(风景,美女)
res = requests.get(url).content
#.text  获取字符串数据  .content  获取二进制数据
#.json()  获取json数据/字典数据
print(res)
#403  禁止访问  404  网址不存在
#200  请求成功  301  302  重定向
#405  请求方式不对
#500  服务器内部错误
#3.保存数据    open('文件名','打开方式').write(数据)
#w 写入文本数据   wb 写入二进制数据
open('2.mp3','wb').write(res)




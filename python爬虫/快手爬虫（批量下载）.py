import requests
#二.用代码批量下载无水印视频
#1.确定数据所在网址
url = '<url id="" type="url" status="" title="" wc="">https://k0u70y2dy1ay2azw2409x8c62xe10x301xx2cz.djvod.ndcimgs.com/upic/2022/01/17/10/BMjAyMjAxMTcxMDM4MDhfMTg2MDIyMDYxM182NTA1NDA4MTEzMV8yXzM=_b_B9d330340b36a5ba0ed3127addb14b6e6.mp4?tag=1-1745240522-unknown-0-vbulgclosb-51782b762d0fd29f&provider=self&clientCacheKey=3x3e7rtn8e23hvu_b.mp4&di=df57977a&bp=10004&ocid=100000302&tt=b&ss=vp</url>'    #找到photoUrl
#2.伪装  把代码伪装成一个正常的游览器或者用户去访问网站
headers = {
    'Cookie': 'kpf=PC_WEB; clientid=3; did=web_9ad8ae6588dc096e3de655da5b1571d7; userId=4729876284; kuaishou.server.webday7_st=ChprdWFpc2hvdS5zZXJ2ZXIud2ViZGF5Ny5zdBKwAUFStUsE2LK_ePP9xqdG5bVSdKIvpGauRs69_a1ZyEelFpmiz-rUnoIkGIqZSUKKpJIvc4n5QB0dXMjyq2dhWiEP2rHXkBCD-q65H1s50no1e4q4amm_zkV2frI9d0njZsVbLm8L8zePOJ5RbGgplMwruOWcC60Ivw-vn-t3ubkkb2QnK8vOj9Dx3LaVfrwU8AUeuNaJHvLmSd8l8D-NXun8FgNJ3eatf4FM0eBfxCgNGhJ9HT6MbGrfdP_lNnYr-H8iHsEiIPpjfm1c4ENRGYPp1oAsDg6-xHHq40jhiW4MRLIxMAV0KAUwAQ; kuaishou.server.webday7_ph=aa21b121f5dd35881fce640e4794c6c8ed8b; kpn=KUAISHOU_VISION',
    'Referer': 'https://www.kuaishou.com/search/video?searchKey=%E5%8E%9F%E7%A5%9E%E7%B2%BE%E5%BD%A9%E7%9E%AC%E9%97%B4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}
data = {
    'operationName': "visionSearchPhoto",
    'query': "fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionSearchPhoto($keyword: String, $pcursor: String, $searchSessionId: String, $page: String, $webPageArea: String) {\n  visionSearchPhoto(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    searchSessionId\n    pcursor\n    aladdinBanner {\n      imgUrl\n      link\n      __typename\n    }\n    __typename\n  }\n}\n",

    'variables': {'keyword': "输入关键字", 'pcursor': "", 'page': "search"} #这里的keyword需要替换成你想要搜索的内容
}

"""
注意：需要将上面的keyword替换成你想要搜索的内容!!!
"""



#3.对目标网站发出请求  获取视频的json数据
res = requests.post(url,headers=headers,json=data).json()
#print(res)
"""
post请求时还需要请求载荷
"""
#4.解析数据  筛选我们真正需要的数据


#第一步先提取整个列表的数据
data_lis = res['data']['visionSearchPhoto']['feeds']
#第二步在爬取每个视频的播放地址
index = 0
for data in data_lis:
    viodie_url = ['photo']['photoUrl']
    #5.对目标网站发出请求  获取视频的二进制数据
    con = requests.get(viodie_url).content
    #6.下载 保存数据
    with open(f'视频名/{index}.mp4','wb') as f:
        f.write(con)
        index += 1

#需要注意的是，下载的视频名需要提前创建好文件夹，否则会报错
#同时需要进行一些必要修改，这段代码并不完全适用于所有视频，需要根据实际情况进行修改



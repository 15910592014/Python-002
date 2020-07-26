# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
# bs4是第三方库需要使用pip命令安装


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)
# print(f'返回码是: {response.status_code}')

bs_info = bs(response.text, 'html.parser')

film_list=[]
for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    atag = tags.find_all('div', attrs={'class': 'movie-hover-title'})
    # 获取电影名称
    film_name = atag[0].find("span", attrs={'class': 'name'}).text
    # 获取电影类型
    film_type = atag[1].text.replace("\n","").split(":")[1].strip()
    # 获取电影上映时间
    film_time = atag[3].text.replace("\n","").split(":")[1].strip()
    film_list.append({
        "电影名称":film_name,
        "电影类型":film_type,
        "上映时间":film_time,
    })

# 格式化数据
mj_result = pd.DataFrame(film_list)

# 写入本地csv文件
mj_result.to_csv('maoyantop10.csv', encoding='utf8', index=False, header=False)




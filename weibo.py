import requests
from lxml import etree
import xlwt

#获取html页面
def get_htmltext(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    try:
        res = requests.get(url,headers=headers)
        res.encoding = 'utf-8'
        return res.text
    except:
        return 'wrong'

#解析提取内容
def parsing_text(data,html):
    #定位
    tree = etree.HTML(html)
    trs = tree.xpath('//div[@class="data"]//tr[position()>1]')
    #循环提取
    for tr in trs:
        info = []
        keyword = tr.xpath('./td[2]/a/text()')[0]
        info.append(keyword)
        num = tr.xpath('./td[2]/span/text()')[0]
        info.append(num)
        #整合到最终列表
        data.append(info)

def save_text(data,path):
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet1')
    col_name = ('关键词','指数')
    for i in range(2):
        ws.write(0,i,col_name[i])
    for r in range(len(data)):
        case = data[r]
        for c in range(2):
            ws.write(r+1,c,case[c])
    wb.save(path)

def main():
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    get_htmltext(url)
    data = []
    html = get_htmltext(url)
    parsing_text(data,html)
    path = '热搜排行榜.xls'
    save_text(data,path)


main()



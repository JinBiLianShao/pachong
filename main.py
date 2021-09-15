import requests

def get_html(url): #爬取源码函数
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4)\
        AppleWebKit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'

    }  # 模拟浏览器访问
    response = requests.get(url, headers=headers)  # 请求访问网站
    response.encoding = response.apparent_encoding #设置字符编码格式
    html = response.text  # 获取网页源码
    return html  # 返回网页源码

if __name__ == '__main__':
    t = get_html("http://127.0.0.1/zhiyuan/")
    t = t.replace("http://127.0.0.1", "https://jinbilianshao.github.io")
    t = t.replace("/index.php/", "/")
    with open('index.html', 'w' ,encoding="utf-8") as s:
        for i in t:
            s.write(i)
import urllib.request
import re
import http.client
import time
import urllib.error


def url_name(url):
    error=''
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    req=urllib.request.Request(url,headers=headers)
    print('即将访问该网页：{}'.format(url))
    try:
        response=urllib.request.urlopen(req,timeout=30)
        html=response.read()
        html = ''.join(html.decode('GBK').split())
    except UnicodeDecodeError as e:
        print("转换{}网页失败，原因{}".format(url,e))
        error=e
    except Exception as e:
        print('未知错误:{}'.format(e))
        error=e
    return html,error

def get_pageCode(url,wfile):
    html=url_name(url)
    fo=open(wfile,'wb')
    fo.write(html)
    fo.close

def get_xing_link():
    with open('pageCode.txt','r',encoding='utf-8') as f:
        line = f.readline()
        while line:
            line=line.split()
            line=''.join(line)
            link=re.findall(r'href="//(.*)name',line)
            print('1:{}'.format(link))
            xing=re.findall(r'共有(.*)姓名字',line)
            print('2:{}'.format(xing))

            if len(link) and len(xing):
                xing_link=xing[0]+','+link[0]
                print('3:{}'.format(xing_link))
                with open('xing_link.txt',mode='a+',encoding='utf-8') as f2:
                    f2.write(xing_link)
                    f2.write('\n')

            line=f.readline()

def get_name():
    with open('xing_link.txt',mode='r',encoding='utf-8') as f:
        line=f.readline()
        while line:
            line=line.strip('\n').split(',')
            xing=line[0]
            link=line[1]
            for sex in ['男','女']:
                if sex == '男':
                    url='http://'+link+'name/boys.html'
                else:
                    url = 'http://' + link + 'name/girls.html'
                wfile='temp'+sex+'.txt'
                n=0
                error=0
                while n<4:
                    try:
                        get_pageCode(url,wfile)
                        error=0
                        break
                    except Exception as e:
                        print("出错：{},重试第{}次".format(e,n+1))
                        error=1
                        n+=1
                if error==1:
                    with open('error.txt',mode='a+',encoding='utf-8') as er:
                        er.write('访问该网页失败：{}'.format(url))
                    continue
                print('开始从临时表中读取该姓信息到name文件:{}'.format(wfile))
                with open(wfile,mode='r',encoding='utf-8') as f1:
                    line1=f1.readline()
                    while line1:
                        line1=''.join(line1.split())
                        _name=re.findall(r'data-name="(.*?)">',line1)
                        if len(_name):
                            str_name=xing+','+sex+','+_name[0]
                            with open('name.txt',mode='a+',encoding='utf-8') as f2:
                                f2.write(str_name)
                                f2.write('\n')
                        line1=f1.readline()
                print('将姓名写入到name文件完成：{},{}'.format(xing,sex))
                print('**********************************************')
            line=f.readline()



def get_address(xingzheng,sheng,num1,name):
    str=','.join([xingzheng,sheng,num1,name])
    with open('address.txt','a+',encoding='utf-8') as f:
        f.write(str)
        f.write('\n')


if __name__ == '__main__':

    # 获取首页信息
    # get_pageCode(url)
    # 获取姓和名字的链接
    # get_xing_link()
    # get_name()
    html,error=url_name('http://www.tcmap.com.cn/list/daima_list.html')
    if error:
        print('出错退出：{}'.format(error))
        exit()
    list=re.findall(r'([0-9]{6,})(<strong>)?<ahref=(.*?)target=_blank>(.*?)</a>',html)
    # print(list)
    for xingzheng,tag,link,num in list:
        # print(xingzheng,tag,link,num)
        if tag:
            sheng=num
        else:
            url='http://www.tcmap.com.cn'+link
            # time.sleep(2)
            html1,error=url_name(url)
            if error:
                print('出错跳过：{}'.format(error))
                continue
            list1=re.findall(r'<strong><ahref=(.*?)class.*?blue>(.*?)</a',html1)

            for link1,num1 in list1:
                # print(xingzheng,num,num1)
                url='http://www.tcmap.com.cn'+link1
                # time.sleep(2)
                html2,error=url_name(url)
                if error:
                    print('出错跳过：{}'.format(error))
                    continue
                list2 = re.findall(r'<strong><ahref=(.*?)class.*?blue>(.*?)</a', html2)
                # print('list2:{}'.format(list2))
                if len(list2) == 0:
                    name = re.findall(r'<h1>(.*?)</h1>', html2)
                    if len(name):
                        get_address(xingzheng, sheng, num, name[0])
                    print('ok:{}'.format(name))
                else:
                    for link2,num2 in list2:
                        # print('link2:{}{}{}{}{}'.format(link2,sheng,num,num1,num2))
                        url = 'http://www.tcmap.com.cn' + link2
                        # time.sleep(2)
                        html3, error = url_name(url)
                        if error:
                            print('出错跳过：{}'.format(error))
                            continue
                        list3 = re.findall(r'<strong><ahref=(.*?)class.*?blue>(.*?)</a', html3)

                        if len(list3) == 0:
                            name=re.findall(r'<h1>(.*?)</h1>',html3)
                            if len(name):
                                get_address(xingzheng, sheng, num, name[0])
                            print('ok:{}'.format(name))
                        else:
                            for link3,num3 in list3:
                                print('link3:{}{}{}{}{}{}'.format(link3, sheng, num, num1, num2,num3))
                                url = 'http://www.tcmap.com.cn' + link3
                                # time.sleep(2)
                                html4, error = url_name(url)
                                if error:
                                    print('出错跳过：{}'.format(error))
                                    continue
                                list4 = re.findall(r'<strong><ahref=(.*?)class.*?blue>(.*?)</a', html4)
                                if len(list4)==0:
                                    name = re.findall(r'<h1>(.*?)</h1>', html4)
                                    if len(name):
                                        get_address(xingzheng, sheng, num, name[0])
                                    # print('ok:{}'.format(name))
                                else:
                                    for link4,num4 in list4:
                                        print(link4, sheng, num, num1, num2,num3,num4)



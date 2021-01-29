import requests

url='https://www.baidu.com/img/bd_logo1.png'

# 响应本身就是一个图片,并且是二进制类型
a=requests.get(url)

#print(a.content)
    
# 以二进制+写入的方式打开文件
with open('baidu.png','wb')as f:
    f.write(a.content)
    # 写入response.content bytes二进制类型至f

##import requests
### 向目标url发送get请求
##r = requests.get("http://www.baidu.com")
### 打印响应内容 r -> response 指的是响应
##print(r.content)
    

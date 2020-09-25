import requests


def test_post_json_1():
    # json类型数据
   data = {
    "pwd": "abc123",
    "userName": "tuu653"
    }
   r = requests.post("http://qa.yansl.com:8084/login",json=data)
   print(r.text)

def test_post_formdata_2(pub_data):
    # post请求键值对数据
   data = {
    "userName": "tan242743"
    }
   h ={"token":pub_data["token"]}
   r = requests.post("http://qa.yansl.com:8084//user/lock",data=data,headers=h)
   print(r.text)

def test_post_upload_file(pub_data):
    # post请求上传文件
    data = {
        "file": open("aa.xls","rb")
    }
    h = {"token": pub_data["token"]}
    r = requests.post("http://qa.yansl.com:8084/product/uploaProdRepertory", files=data, headers=h)
    print(r.text)

def test_post_json_1(pub_data):
    data = {
            "pwd": "wh123456",
            "userName": "wh1kxd82"
    }
    h = {"token": pub_data["token"]}
    r = requests.post("http://qa.yansl.com:8084/login", json=data, headers=h)  # json关键字发送json类型数据
    print("请求方法:",r.request.method)
    print("url:", r.request.url)
    print("请求头:", r.request.headers)
    print("请求正文:", r.request.body)
    print("响应状态码:",r.status_code)
    print("响应头:",r.headers)
    print("响应正文:", r.text)

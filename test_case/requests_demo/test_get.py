import allure
import requests

@allure.feature("get请求")
@allure.story("无参数")
@allure.title("用例名1")
def test_no_params():
    # 使用requests.get发送一个get请求...无参数
    r = requests.get("https://www.baidu.com/")
    print(r.text)
def test_no_params_l():
    r = requests.request(method="GET",url="https://www.baidu.com/")
    print(r.text)
@allure.feature("get请求")
@allure.story("无参数2")
@allure.title("用例名2")
def test_no_params_ll():
    sess = requests.session()
    r = sess.request(method="GET",url="https://www.baidu.com/")
    print(r.text)

def test_get_query():
    # get请求参数在path中
    r = requests.request("GET","https://qa.yansl.com:8084/acc/selAllAccs/{}/{}".format(1,10))
    print(r.text)

@allure.feature("get请求")
@allure.story("get请求带参数")
@allure.title("用例名3")
def test_get_path_c():
    # get请求带参数
    pa = {"accountName":"xuepl123"}
    r = requests.get("http://qa.yansl.com:8084/acc/getAccInfo",params=pa)
    print(r.text)

@allure.feature("get请求")
@allure.story("path请求带参数")
@allure.title("用例名4")
def test_get_path_cs():
        # get 请求参数在path中，使用.format进行字符串格式化
    r = requests.get("http://qa.yansl.com:8084/acc/getAllAccs/{}/{}".format(1,10))
    print(r.text)
@allure.feature("get请求")
@allure.story("下载文件")
@allure.title("用例名5")
def test_get_file(pub_data):
    # get请求下载文件
    with allure.step("第一步、准备测试数据"):pass
    p = {"pridCode":"63803y"}
    h = {"token":pub_data["token"]}
    with allure.step("第二步、发送请求"):pass
    r = requests.get("http://qa.yansl.com:8084/product/downProdRepertory",params=p,headers=h)
    with allure.step("第三步、请求数据"):
        allure.attach("请求行，请求头，请求正文","请求信息",allure.attachment_type.TEXT)
    with open("aa.xls","wb")as f:
        f.write(r.content)

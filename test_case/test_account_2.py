import random

from tools.api import request_tool
import pytest
from tools.data import excel_tool
@pytest.mark.smoke
def test_get_customer(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询单个用户'  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/cst/getCustomer"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"phone":'18103909786'}
    headers={"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)

@pytest.mark.smoke
def test_get_all_customer(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '查询所有用户'  # allure报告中二级分类
    title = "全量查询"  # allure报告中用例名字
    uri = "/cst/getAll/{}/{}".format(1,10)  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = None
    headers={"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)


@pytest.mark.smoke
def test_get_file(pub_data):
    file_name = "e:\\aaa.xlsx" # 下载文件地址
    method = "GET"  #请求方法，全部大写
    feature = "库存模块"  # allure报告中一级分类
    story = '下载库存信息'  # allure报告中二级分类
    title = "下载库存信息_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/downProdRepertory"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"pridCode":'oioq649'}
    headers = {"token": "${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
    with open(file_name,"wb") as f :
        f.write(r.content)
@pytest.mark.smoke

def test_post_file(pub_data):
    file_name = "e:\\aaa.xlsx" # 上载文件地址
    method = "POST"  #请求方法，全部大写
    feature = "库存模块"  # allure报告中一级分类
    story = '盘点库存'  # allure报告中二级分类
    title = "盘点库存"  # allure报告中用例名字
    uri = "/product/uploaProdRepertory"  # 接口地址
# post请求json数据，注意数据格式为字典或者为json串 为空写None
    files = {"file":open(file_name,'rb')}
    headers={"token":"${token}"}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,files=files,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)




data = excel_tool.get_test_case("E:\\充值接口测试.xls")
@pytest.mark.parametrize("accountname,changeMoney,expect",data[1],ids=data[0])
def test_post_json(pub_data,accountname,changeMoney,expect):
    pub_data["accountname"] = accountname
    pub_data["changeMoney"] = changeMoney
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '充值'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
  {
  "accountName": "${accountname}",
  "changeMoney": "${changeMoney}"
}
    '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
#
data = excel_tool.get_test_case("E:\\tixian.xls")
@pytest.mark.parametrize("accountname,cardno,changemoney",data[1],ids=data[0])
def test_post_json_m(pub_data,accountname,cardno,changemoney):
    pub_data["accountname"] = accountname
    pub_data["cardno"] = cardno
    pub_data["changemoney"] = changemoney
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '提现'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/withdraw"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "accountName": "${accountname}",
  "cardNo": "${cardno}",
  "changeMoney": "${changemoney}"
} '''
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)


print('57458484')


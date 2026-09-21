import pytest
import json
from common.http_client import HttpClient
from utils.read_excel import read_test_cases

# 读取 Excel 里的测试数据
cases = read_test_cases("data/test_cases.xlsx")


@pytest.fixture(scope="module")
def client():
    """创建 HttpClient 实例，供所有测试用例使用"""
    return HttpClient(base_url="https://httpbin.org")


@pytest.mark.parametrize("case", cases, ids=[c["用例编号"] for c in cases])
def test_api(client, case):
    """数据驱动：根据 Excel 里的每一行数据，自动生成一个测试用例"""
    method = case["请求方法"]
    path = case["请求路径"]
    expected_status = case["期望状态码"]
    params = case["请求参数"]

    # 解析 JSON 参数（Excel 里存的是字符串）
    kwargs = {}
    if params:
        kwargs["json"] = json.loads(params)

    # 根据请求方法，动态调用对应的方法
    if method == "GET":
        response = client.get(path, **kwargs)
    elif method == "POST":
        response = client.post(path, **kwargs)
    elif method == "PUT":
        response = client.put(path, **kwargs)
    elif method == "DELETE":
        response = client.delete(path, **kwargs)
    else:
        pytest.fail(f"不支持的请求方法: {method}")

    # 断言状态码
    assert response.status_code == expected_status, \
        f"用例 {case['用例编号']} 失败：期望 {expected_status}，实际 {response.status_code}"
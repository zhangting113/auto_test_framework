import pytest
import json
import allure
from common.http_client import HttpClient
from utils.read_excel import read_test_cases

cases = read_test_cases("data/test_cases.xlsx")


@pytest.fixture(scope="module")
def client():
    return HttpClient(base_url="https://httpbin.org")


@allure.feature("接口自动化测试")
class TestAPI:

    @allure.story("数据驱动接口测试")
    @pytest.mark.parametrize("case", cases, ids=[c["用例编号"] for c in cases])
    def test_api(self, client, case):
        allure.dynamic.title(f"{case['用例编号']} - {case['接口名称']}")

        method = case["请求方法"]
        path = case["请求路径"]
        expected_status = case["期望状态码"]
        params = case["请求参数"]

        kwargs = {}
        if params:
            kwargs["json"] = json.loads(params)

        with allure.step(f"发送 {method} 请求到 {path}"):
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

        with allure.step(f"断言状态码为 {expected_status}"):
            assert response.status_code == expected_status, \
                f"用例 {case['用例编号']} 失败：期望 {expected_status}，实际 {response.status_code}"
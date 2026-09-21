import pytest
from common.http_client import HttpClient


@pytest.fixture(scope="module")
def client():
    """创建 HttpClient 实例，供所有测试用例使用"""
    return HttpClient(base_url="https://httpbin.org")


def test_get_request(client):
    """测试 GET 请求是否正常返回"""
    response = client.get("/get")
    assert response.status_code == 200
    print(f"响应内容: {response.json()}")


def test_post_request(client):
    """测试 POST 请求是否正常返回"""
    data = {"name": "zhangting", "action": "test"}
    response = client.post("/post", json=data)
    assert response.status_code == 200
    assert response.json()["json"]["name"] == "zhangting"
from common.http_client import HttpClient

client = HttpClient(base_url="https://httpbin.org")

response = client.get("/get")
print(f"状态码: {response.status_code}")
print(f"返回内容: {response.text}")
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class HttpClient:
    """封装 HTTP 请求，统一处理请求头、超时、日志"""

    def __init__(self, base_url=""):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": "AutoTestFramework/1.0"
        })

    def send_request(self, method, url, **kwargs):
        full_url = self.base_url + url
        logger.info(f"请求: {method} {full_url}")
        try:
            response = self.session.request(method, full_url, timeout=10, **kwargs)
            logger.info(f"响应状态码: {response.status_code}")
            return response
        except requests.exceptions.Timeout:
            logger.error(f"请求超时: {full_url}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"请求异常: {e}")
            raise

    def get(self, url, **kwargs):
        return self.send_request("GET", url, **kwargs)

    def post(self, url, **kwargs):
        return self.send_request("POST", url, **kwargs)

    def put(self, url, **kwargs):
        return self.send_request("PUT", url, **kwargs)

    def delete(self, url, **kwargs):
        return self.send_request("DELETE", url, **kwargs)
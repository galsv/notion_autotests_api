import logging
from requests import Session, Response
from curlify import to_curl
from notion_autotest_api.utils.allure.logger import allure_logger


class BaseSession(Session):
    def __init__(self, url, notion_version, bearer_token):
        super(BaseSession, self).__init__()
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',
            'Notion-Version': f'{notion_version}',
            'Authorization': f'Bearer {bearer_token}',
        }

    @allure_logger
    def request(self, method, url, **kwargs) -> Response:
        response = super().request(method, self.url + url, headers=self.headers, **kwargs)
        logging.info(f'{response.status_code} {to_curl(response.request)}')

        return response

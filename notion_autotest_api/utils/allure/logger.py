import json
from json import JSONDecodeError

import allure
from allure_commons.types import AttachmentType
from requests import Response
from curlify import to_curl


def allure_logger(function):
    def wrapper(*args, **kwargs):
        method, url = args[1], args[2]

        with allure.step(f"{method} {url}"):
            response: Response = function(*args, **kwargs)

            allure.attach(body=to_curl(response.request).encode("utf8"),
                          name=f"Request {response.status_code}",
                          attachment_type=AttachmentType.TEXT,
                          extension=".txt")
            try:
                allure.attach(body=json.dumps(response.json(), indent=4).encode("utf8"),
                              name=f"Response {response.status_code}",
                              attachment_type=AttachmentType.JSON,
                              extension=".json")
            except JSONDecodeError:
                allure.attach(body=response.text.encode("utf8"),
                              name=f"Response {response.status_code}",
                              attachment_type=AttachmentType.TEXT,
                              extension=".txt")

        return response

    return wrapper

from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class BlockType(ExtendedEnum):
    ChildPage = 'child_page'
    ChildDatabase = 'child_database'
    Heading_2 = 'heading_2'
    Paragraph = 'paragraph'
    Code = 'code'
    Image = 'image'
    TODO = 'to_do'


def heading_2(content: str):
    return {
        "rich_text": [
            {
                "type": "text",
                "text": {
                    "content": content
                }
            }
        ]
    }


def paragraph(content: str, url: str):
    return {
        "rich_text": [
            {
                "type": "text",
                "text": {
                    "content": content,
                    "link": {
                        "url": url
                    }
                }
            }
        ]
    }


def code(content: str, language: str):
    return {
        "caption": [],
        "rich_text": [{
            "type": "text",
            "text": {
                "content": content
            }
        }],
        "language": language
    }


def image(url: str):
    return {
        "type": "external",
        "external": {
            "url": url
        }
    }


def to_do(content: str, checked: bool):
    return {
        "rich_text": [
            {
                "type": "text",
                "text": {
                    "content": content,
                    "link": None
                }
            }
        ],
        "checked": checked,
        "color": "default"
    }

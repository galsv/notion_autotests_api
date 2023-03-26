import os
from dotenv import load_dotenv
from enum import Enum
from dataclasses import dataclass
from notion_autotest_api.data.page import block
from notion_autotest_api.data.block import BlockType, heading_2, paragraph, code, image, to_do


class Object(Enum):
    Block = 'block'
    Page = 'page'
    Databases = 'database'


@dataclass
class MainAttribute:
    url: str
    version: str
    token: str
    parent_page: str


load_dotenv()
main_attribute = MainAttribute(os.getenv('NOTION_URL'),
                               os.getenv('NOTION_VERSION'),
                               os.getenv('NOTION_TOKEN'),
                               os.getenv('PARENT_PAGE'))

title = 'Page Test Title'
title_update = 'Page Update Title'

children_page_blocks = [
    block(BlockType.Heading_2, heading_2('Heading 2')),
    block(BlockType.Paragraph, paragraph('Wikipedia', 'https://en.wikipedia.org/')),
    block(BlockType.Image, image('https://raw.githubusercontent.com/galsv/qa_guru_python_5/main/test_pic.png')),
    block(BlockType.Code, code('print("Hello, world!")', 'python')),
    block(BlockType.TODO, to_do('test', True))
]

database_title = 'Grocery List'


def grocery_list() -> dict:
    return {
        "Name": {
            "title": {}
        },
        "Description": {
            "rich_text": {}
        },
        "In stock": {
            "checkbox": {}
        },
        "Food group": {
            "select": {
                "options": [
                    {
                        "name": "🥦Vegetable",
                        "color": "green"
                    },
                    {
                        "name": "🍎Fruit",
                        "color": "red"
                    },
                    {
                        "name": "💪Protein",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Price": {
            "number": {
                "format": "dollar"
            }
        },
        "Last ordered": {
            "date": {}
        },
        "Store availability": {
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "name": "Duc Loi Market",
                        "color": "blue"
                    },
                    {
                        "name": "Rainbow Grocery",
                        "color": "gray"
                    },
                    {
                        "name": "Nijiya Market",
                        "color": "purple"
                    },
                    {
                        "name": "Gus's Community Market",
                        "color": "yellow"
                    }
                ]
            }
        },
        "+1": {
            "people": {}
        },
        "Photo": {
            "files": {}
        }
    }

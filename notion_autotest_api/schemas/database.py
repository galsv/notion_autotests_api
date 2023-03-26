from voluptuous import Schema, PREVENT_EXTRA
from notion_autotest_api.schemas.page import create_edit


create_database = Schema(
    {
        "object": "database",
        "id": str,
        "cover": None,
        "icon": None,
        "created_time": str,
        "created_by": create_edit,
        "last_edited_by": create_edit,
        "last_edited_time": str,
        "title": [
            {
                "type": "text",
                "text": {
                    "content": str,
                    "link": None
                },
                "annotations": {
                    "bold": bool,
                    "italic": bool,
                    "strikethrough": bool,
                    "underline": bool,
                    "code": bool,
                    "color": str
                },
                "plain_text": str,
                "href": None
            }
        ],
        "description": [],
        "is_inline": bool,
        "properties": dict,
        "parent": {
            "type": str,
            "page_id": str
        },
        "url": str,
        "archived": bool
    },
    extra=PREVENT_EXTRA,
    required=True
)

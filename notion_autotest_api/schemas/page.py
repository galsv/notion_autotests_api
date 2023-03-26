from voluptuous import PREVENT_EXTRA, REMOVE_EXTRA, Schema, Optional

create_edit = Schema(
    {
        "object": str,
        "id": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

parent = Schema(
    {
        "type": str,
        "page_id": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

properties = Schema(
    {
        "title": {
            "id": str,
            "type": str,
            "title": [
                {
                    "type": str,
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
            ]
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)

create_page = Schema(
    {
        "object": str,
        "id": str,
        "created_time": str,
        "last_edited_time": str,
        "created_by": create_edit,
        "last_edited_by": create_edit,
        "cover": None,
        "icon": None,
        "parent": parent,
        "archived": bool,
        "properties": properties,
        "url": str,
        "has_children": bool,
        "type": str,
        "child_page": {
            "title": str
        }
    },
    extra=REMOVE_EXTRA
)


block_s = Schema(
    {
        "object": str,
        "id": str,
        "parent": parent,
        "created_time": str,
        "last_edited_time": str,
        "created_by": create_edit,
        "last_edited_by": create_edit,
        "has_children": bool,
        "archived": bool,
        "type": str,
        Optional("heading_2"): dict,
        Optional("paragraph"): dict,
        Optional("image"): dict,
        Optional("code"): dict,
        Optional("to_do"): dict,
        Optional("child_database"): dict

    },
    extra=PREVENT_EXTRA,
    required=True
)

add_blocks = Schema(
    {
        "object": str,
        "results": [block_s],
        "next_cursor": None,
        "has_more": bool,
        "type": str,
        "block": dict
    },
    extra=PREVENT_EXTRA,
    required=True
)

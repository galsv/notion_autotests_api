def create_with_structure(parent_id: str, title: str, properties: dict):
    return {
        "parent": {
            "type": "page_id",
            "page_id": parent_id
        },
        "title": [
            {
                "type": "text",
                "text": {
                    "content": title,
                    "link": None
                }
            }
        ],
        "properties": properties
    }

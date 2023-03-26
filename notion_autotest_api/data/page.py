from notion_autotest_api.data.block import BlockType


def properties(title: str) -> dict:
    return {
        "title": {
            "id": "title",
            "type": "title",
            "title": [
                {
                    "text": {
                        "content": f"{title}"
                    }
                }
            ]
        }
    }


def create_without_blocks(parent_id: str, title: str) -> dict:
    return {
        "parent": {
            "page_id": f"{parent_id}"
        },
        "properties": properties(title)
    }


def add_blocks(blocks: list):
    return {
        "children": blocks
    }


def block(block_type: BlockType, block_value: dict):
    return {
        "object": "block",
        "type": block_type.value,
        block_type.value: block_value
    }

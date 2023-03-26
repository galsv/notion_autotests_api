from notion_autotest_api.utils.base_session import BaseSession
from notion_autotest_api.data.notion import Object, main_attribute
from notion_autotest_api.data import page, database
from notion_autotest_api.data.block import BlockType


class Notion:
    def __init__(self):
        self.session = BaseSession(main_attribute.url,
                                   main_attribute.version,
                                   main_attribute.token)

    def retrieve(self, notion_object: Object, object_id: str):
        return self.session.get(f'/v1/{notion_object.value}s/{object_id}')

    def retrieve_blocks(self, page_id: str, page_size: int):
        return self.session.get(f'/v1/blocks/{page_id}/children', params={'page_size': page_size})

    def add_page_without_blocks(self, parent_id: str, title: str):
        json = page.create_without_blocks(parent_id, title)
        return self.session.post('/v1/pages/', json=json)

    def add_database(self, parent_id: str, title: str, properties: dict):
        json = database.create_with_structure(parent_id, title, properties)
        return self.session.post('/v1/databases/', json=json)

    def add_blocks(self, page_id: str, blocks: list):
        json = page.add_blocks(blocks)
        return self.session.patch(f'/v1/blocks/{page_id}/children', json=json)

    def update_page_title(self, page_id: str, title: str):
        json = {
            'properties': page.properties(title)
        }
        return self.session.patch(f'/v1/pages/{page_id}', json=json)

    def update_block(self, block_id: str, block_type: BlockType, block: dict):
        json = {
            block_type.value: block
        }
        return self.session.patch(f'/v1/blocks/{block_id}', json=json)

    def delete(self, object_id: str):
        return self.session.delete(f'/v1/blocks/{object_id}')

    def return_first_by_block_type(self, block_type: BlockType, parent_id=main_attribute.parent_page, find_size=100):
        response = self.retrieve_blocks(parent_id, find_size)
        for block in response.json().get('results'):
            if block.get('type') == block_type.value:
                return block
        return None


notion = Notion()

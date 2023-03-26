import pytest
import allure

from pytest_voluptuous import S
from notion_autotest_api.framework.notion import notion
from notion_autotest_api.data.block import BlockType, heading_2
from notion_autotest_api.schemas.page import create_page, add_blocks, block_s
from notion_autotest_api.data.notion import main_attribute, \
                                            title, \
                                            title_update, \
                                            children_page_blocks


@allure.title('Add children page')
def test_create():
    response = notion.add_page_without_blocks(main_attribute.parent_page, title)

    assert response.status_code == 200
    assert S(create_page) == response.json()
    assert response.json()['properties']['title']['title'][0]['text']['content'] == title


@allure.title('Change children page\'s title')
@pytest.mark.parametrize('title_name', [title_update, title])
def test_update_tittle(find_page, title_name):
    child_page = find_page

    response = notion.update_page_title(child_page.get('id'), title_name)
    assert response.status_code == 200
    assert S(create_page) == response.json()
    assert title_name.replace(' ', '-') in response.json().get('url')


@allure.title('Add list of blocks on children page')
def test_add_blocks(find_page):
    child_page = find_page

    response = notion.add_blocks(child_page.get('id'), children_page_blocks)
    assert response.status_code == 200
    assert S(add_blocks) == response.json()


@allure.title('Update heading on children page')
def test_update_block(find_page):
    child_page = find_page
    heading_name = 'New Heading'
    block_type = BlockType.Heading_2
    block = notion.return_first_by_block_type(block_type, child_page.get('id'), 100)
    assert block is not None

    response = notion.update_block(block.get('id'), block_type, heading_2(heading_name))
    assert response.status_code == 200
    assert S(block_s) == response.json()
    assert response.json()[block_type.value]['rich_text'][0]['text']['content'] == heading_name


@allure.title('Delete all blocks from children page')
def test_delete_block(find_page):
    child_page = find_page
    blocks = notion.retrieve_blocks(child_page.get('id'), page_size=100).json().get('results')
    assert len(blocks) != 0

    for block in blocks:
        if block.get('type') in BlockType.list():
            response = notion.delete(block.get('id'))
            assert response.status_code == 200
            assert S(block_s) == response.json()


@allure.title('Delete page from parent page')
def test_delete(find_page):
    child_page = find_page

    response = notion.delete(child_page.get('id'))

    assert response.status_code == 200
    assert S(create_page) == response.json()

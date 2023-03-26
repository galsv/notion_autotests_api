import allure

from notion_autotest_api.framework.notion import notion
from notion_autotest_api.data.block import BlockType
from notion_autotest_api.schemas.database import create_database
from notion_autotest_api.schemas.page import block_s
from notion_autotest_api.data.notion import main_attribute, grocery_list, database_title
from pytest_voluptuous import S


@allure.title('Add children database')
def test_create():
    response = notion.add_database(main_attribute.parent_page, database_title, grocery_list())
    assert response.status_code == 200
    assert S(create_database) == response.json()


@allure.title('Delete children database from parent page')
def test_delete():
    database = notion.return_first_by_block_type(BlockType.ChildDatabase)
    assert database is not None

    response = notion.delete(database.get('id'))
    assert response.status_code == 200
    assert S(block_s) == response.json()

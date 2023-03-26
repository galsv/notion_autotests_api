import pytest
from dotenv import load_dotenv
from notion_autotest_api.framework.notion import notion
from notion_autotest_api.data.block import BlockType


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def find_page():
    find_page = notion.return_first_by_block_type(BlockType.ChildPage)
    assert find_page is not None
    return find_page

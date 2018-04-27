"""
Настройки тестов для генератора.

"""
import pytest


# @pytest.fixture(scope="session")
# def django_db_setup(django_db_setup, django_db_blocker):
#     """
#     Грузим фикстуры для тестов.
#
#     """
#     with django_db_blocker.unblock():
#         call_command("loaddata", "apps/generator/tests/fixtures/test_data.json")


def generate_random_paths(max_depth_folder, max_depth_files, folder=False, files=False,
                          max_files_level_count=5, max_folders_level_count=5):
    """
    Генерирует случайно папки и файлы по вложенности.
    Возвращает два словаря с вложенностью.

    :param max_depth_folder:
    :param max_depth_files:
    :param folder:
    :param files:
    :param max_files_level_count:
    :param max_folders_level_count:

    :return:

    """
    pass


@pytest.fixture(scope='session')
def random_formula():
    """
    Формирует и возвращает функцию, которая генерирует файлы и папки любой вложенности.


    """
    pass

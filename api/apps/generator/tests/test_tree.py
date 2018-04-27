"""
Тестирование дерева.

"""
import pytest
import random

from ..tree import Node, Tree


class TestTreeCreate(object):
    """
    Тестирование создания дерева.

    """
    def __test_default_node(self, node, path=None, type_node=None, count_folders=None, count_files=None):
        """
        Станартная проверка ноды.

        :param Node node: Сама надо для проверки.
        :param str path: Ожидаемый путь в ноде. Если не передано не проверяется.
        :param str type_node: Ожидаемый тип ноды. Если не передано не проверяется.
        :param int count_folders: Ожидаемое кол-во папок. Если не передано не проверяется.
        :param int count_files: Ожидаемое кол-во файлов. Если не передано не проверяется.

        """
        assert isinstance(node, Node)
        if path is not None:
            assert node.path == path
        if type_node is not None:
            assert node.type_node == type_node
        if count_folders is not None:
            assert len(node.folders) == count_folders
        if count_files is not None:
            assert len(node.files) == count_files

    def __test_default_tree(self, tree, count_folders=None, count_files=None):
        """
        Стандартная проверка атирбутов для дерева.
        Работает для каждого тества.

        :param Tree tree: Дерево которое нужно проверить.
        :param int count_folders: Ожидаемое кол-во папок. Если не передано то не проверяется.
        :param int count_files: Ожидаемое кол-во файлов. Если не передано то не проверяется.

        """
        # Смотрим что все создалось как надо.
        assert isinstance(tree.root, Node)
        assert isinstance(tree.root.folders, dict)
        assert isinstance(tree.root.files, dict)
        assert tree.root.type_node == 'folder'
        assert tree.root.path == ''
        if count_folders is not None:
            assert len(tree.root.folders) == count_folders
        if count_files is not None:
            assert len(tree.root.files) == count_files

    def test_create_empty(self):
        """
        Тестирование создания без файлов и папок.

        """
        tree = Tree()
        self.__test_default_tree(tree, 0, 0)

    def test_create_folder_not_include(self):
        """
        Тестирование создания с папками без вложенности.

        """
        folders = ['123', '123', '234', '234', '345', '456']
        tree = Tree(folders=folders)
        self.__test_default_tree(tree, 4, 0)
        # Смотрим что папки создались хорошо.
        for _f, node in tree.root.folders.items():
            assert _f in folders
            self.__test_default_node(node, _f, 'folder', 0, 0)

    def test_create_folders_easy(self):
        """
        Создание с папками максимальной вложенности 2.

        """
        # Сначала готовим даные.
        folders = {'123': ['123', '234'], '234': ['123', '234'], '345': ['123'], '456': ['456']}
        folders_list = []
        # Понятный для дерева список.
        for k, val in folders.items():
            folders_list.extend(['/'.join((k, v)) for v in val])

        tree = Tree(folders=folders_list)

        self.__test_default_tree(tree, 4, 0)
        # Смотрим что папки создались хорошо.
        for _f, _node in tree.root.folders.items():
            assert _f in folders
            self.__test_default_node(_node, _f, 'folder', len(folders[_f]), 0)
            # Теперь юежим по второму уровню.
            for __f, __node in _node.folders.items():
                assert __f in folders[_f]
                self.__test_default_node(__node, '/'.join((_f, __f)), 'folder', 0, 0)

    def test_create_folders_middle(self):
        """
        Создание с папками максимальной вложенности 5.

        """
        # Сначала готовим даные.
        folders = {}
        for _ in range(10):
            _b_folder = str(random.randint(1, 999))
            folders[_b_folder] = {}

        folders_list = []
        # Понятный для дерева список.
        for k, val in folders.items():
            folders_list.extend(['/'.join((k, v)) for v in val])

        tree = Tree(folders=folders_list)

        self.__test_default_tree(tree, 4, 0)
        # Смотрим что папки создались хорошо.
        for _f, _node in tree.root.folders.items():
            assert _f in folders
            self.__test_default_node(_node, _f, 'folder', len(folders[_f]), 0)
            # Теперь юежим по второму уровню.
            for __f, __node in _node.folders.items():
                assert __f in folders[_f]
                self.__test_default_node(__node, '/'.join((_f, __f)), 'folder', 0, 0)

    def test_create_folders_hard(self):
        """
        Создание с папками максимальной вложенности 10.

        """
        pass

    def test_create_files_easy(self):
        pass

    def test_create_files_middle(self):
        pass

    def test_create_files_hard(self):
        pass

    def test_create_folders_and_files_easy(self):
        pass

    def test_create_folders_and_files_middle(self):
        pass

    def test_create_folders_and_files_hard(self):
        pass

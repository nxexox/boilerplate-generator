"""
Дерево файлов и папок.

"""


class Node(object):
    """
    Единичная нода. Папка или файл.

    """
    def __init__(self, type_node, path, folders=None, files=None):
        """
        Создание ноды.

        :param str type_node: Тип ноды: file, folder.
        :param str path: Полный путь до файла/папки.
        :param dict folders: Вложенные папки.
        :param dict files: Вложенные файлы.

        """
        self.type_node = type_node
        self.path = path
        self.folders = folders if folders else {}
        self.files = files if files else {}

    def __str__(self):
        return f'{self.path} - ({self.type_node})'

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            'type_node={}, path={}, folders={}, files={}'.format(
                f'"{self.type_node}"',
                f'"{self.path}"',
                f'{self.folders}',
                f'{self.files}'
            )
        )


class Tree(object):
    """
    Дерево нод и папок.

    """
    def __init__(self, files=None, folders=None):
        """
        Строит дерево файлов и папок.

        :param iter files: Список файлов на проекте. Список dict объектов.
        :param iter folders: Список папок на проекте. Список dict объектов.

        """
        # Сначала сортируем по вложенности, что бы сначала минимум вложенности создать а потом максимум.
        self.__files = sorted(files, key=lambda x: x.count('/')) if files else []
        self.__folders = sorted(folders, key=lambda x: x.count('/')) if folders else []

        self.root = Node('folder', '')

        # Создаем папки.
        for _f in self.__folders:
            self.__create_folder(_f)

    def __create_folder(self, full_path):
        """
        Создает Ноду папку, и все вложенные. Т.е. полный путь.
        Возвращает верхнюю ноду.

        :param str full_path: Полный путь для папки.

        :return: Готовая нода.
        :rtype: Node

        """
        if self.__check_folder(full_path):
            return self.get_parent_folder(full_path)

        path = self.__clean_path(full_path)
        __folders = path.split('/')
        now_node = self.root
        _now_path = []

        for _f in __folders:
            _now_path.append(_f)
            __path = '/'.join(_now_path)
            if _f in now_node.folders:
                now_node = now_node.folders[_f]
            else:
                now_node.folders[_f] = Node('folder', __path)
                now_node = now_node.folders[_f]

        return self.root

    def __check_folder(self, folder):
        """
        Проверяет наличие и занятость папки.

        :param str folder: Путь до папки для проверки.

        :return: Результа проверки. Занята ли папка?
        :rtype: bool

        """
        # Сначала чистим путь и разбиваем его.
        folders = self.__clean_path(folder).split('/')
        now_node = self.root

        # Теперь бежим по папкам начиная сверху, и пробуем искать каждую.
        for f in folders:
            # Если папки нет, то исктаь дальше нет смысла.
            if f not in now_node.folders:
                return False
            # Иначе спускамемся на уровень ниже.
            now_node = now_node.folders[f]

        return True

    def __clean_path(self, path):
        """
        Очищает путь от / вначале и конце пути.

        :param str path: путь который стоит почистить.

        :return: Очищенный путь.
        :rtype: str

        """
        if path.startswith('/'):
            path = path[1:]
        if path.endswith('/'):
            path = path[:-1]

        return path

    def get_parent_folder(self, path):
        """
        Возвращает главную в иерархии папку.

        :param str path: Полный путь до папки.

        :return: Главная в иерархии папка.
        :rtype: Node

        """
        folders = self.__clean_path(path).split('/')

        if folders[0] in self.root.folders:
            return self.root.folders[folders[0]]

        return None

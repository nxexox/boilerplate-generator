"""
Сериалайзеры для работы генератора.

"""
from rest_framework import serializers

from . import models


class ProgrammingLanguageCodeListReadSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для чтения языка.

    """
    class Meta:
        model = models.ProgrammingLanguageCode
        fields = 'language', 'extension'


class ProgrammingLanguageCodeCreateSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для создания языка.

    """
    class Meta:
        model = models.ProgrammingLanguageCode
        fields = 'language', 'extension'


class FolderListReadSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для списка папок.

    """
    class Meta:
        model = models.Folder
        fields = 'boilerplate', 'path'
        depth = 1


class FolderRetrieveReadSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для конкретной папки.

    """
    class Meta:
        model = models.File
        fields = 'boilerplate', 'path'
        depth = 1


class FileListReadSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для списка файлов.

    """
    class Meta:
        model = models.File
        fields = 'boilerplate', 'programming_language', 'path'
        depth = 1


class FileRetrieveReadSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для конкретного файла.

    """
    class Meta:
        model = models.File
        fields = 'boilerplate', 'programming_language', 'path', 'content'
        depth = 1

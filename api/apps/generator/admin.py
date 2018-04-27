from django.contrib import admin

from . import models


@admin.register(models.ProgrammingLanguageCode)
class ProgrammingLanguageCodeAdmin(admin.ModelAdmin):
    """
    Типы файлов.

    """
    list_display = 'language', 'extension'
    list_display_links = 'language', 'extension'
    search_fields = 'language', 'extension'


@admin.register(models.Boilerplate)
class BoilerplateAdmin(admin.ModelAdmin):
    """
    Булерплейт.

    """
    list_display = 'id', 'name',
    list_display_links = 'id', 'name'
    search_fields = 'id', 'name'


@admin.register(models.Folder)
class FolderAdmin(admin.ModelAdmin):
    """
    Папка в булерплейте.

    """
    list_display = 'id', 'path', 'boilerplate'
    list_display_links = 'id', 'path', 'boilerplate'
    search_fields = 'id', 'path', 'boilerplate__name'
    list_select_related = 'boilerplate',


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    """
    Файл в булерплейте.

    """
    list_display = 'id', 'path', 'boilerplate', 'programming_language'
    list_display_links = 'id', 'path', 'boilerplate', 'programming_language'
    search_fields = (
        'id', 'path', 'boilerplate__name', 'programming_language__language', 'programming_language__extension'
    )
    list_select_related = 'boilerplate', 'programming_language'

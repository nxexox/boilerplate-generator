"""
Пишем модели для генератора.

"""
from django.db import models

from apps.utils.models import DateTimeAutoModelMixin


class ProgrammingLanguageCode(DateTimeAutoModelMixin, models.Model):
    """
    Тип файлов.

    """
    language = models.CharField('Название языка', max_length=255)
    extension = models.CharField('Расширение файла', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Тип файла'
        verbose_name_plural = 'Типы файлов'

    def __str__(self):
        return self.language


class Boilerplate(DateTimeAutoModelMixin, models.Model):
    """
    Сам бойлерплейт.

    """
    name = models.CharField('Название', max_length=255, null=True)

    class Meta:
        verbose_name = 'Бойлерплейт'
        verbose_name_plural = 'Бойлерплейты'

    def __str__(self):
        return self.name


class Folder(models.Model):
    """
    Папка в бойлерплейте.

    """
    boilerplate = models.ForeignKey(Boilerplate, verbose_name='Бойлерплаейт', related_name='folders')
    path = models.TextField('Путь до папки от корня')

    class Meta:
        verbose_name = 'Папка в булерплейте'
        verbose_name_plural = 'Папки в булерплейте'
        unique_together = ('boilerplate', 'path')

    def __str__(self):
        return self.path


class File(DateTimeAutoModelMixin, models.Model):
    """
    Файл в бойлерплейте.

    """
    boilerplate = models.ForeignKey(Boilerplate, verbose_name='Бойлерплаейт', related_name='files')
    programming_language = models.ForeignKey(ProgrammingLanguageCode, verbose_name='Тип файла', related_name='files')

    path = models.TextField('Путь до файла от корня', null=False)

    content = models.TextField('Содержимое файла', null=True)

    class Meta:
        verbose_name = 'Файл в булерплейте'
        verbose_name_plural = 'Файлы в булерплейте'
        unique_together = ('boilerplate', 'path')

    def __str__(self):
        return self.path

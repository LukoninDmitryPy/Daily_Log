from django.db import models

# Create your models here.


class Calendar(models.Model):
    times = models.DateTimeField()
    
class Note(models.Model):
    text = models.TextField(
        'Текст заметки',
        help_text='Введите текст заметки',
    )
    time = models.ForeignKey(
        Calendar,
        on_delete=models.CASCADE,
        related_name='note',
        verbose_name='Запись',
        help_text='Запись часа',
    )
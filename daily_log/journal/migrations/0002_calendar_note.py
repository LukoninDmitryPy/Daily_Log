# Generated by Django 4.2.4 on 2023-08-31 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='note',
            field=models.ForeignKey(default=1, help_text='Запись часа', on_delete=django.db.models.deletion.CASCADE, related_name='note', to='journal.note', verbose_name='Запись'),
            preserve_default=False,
        ),
    ]

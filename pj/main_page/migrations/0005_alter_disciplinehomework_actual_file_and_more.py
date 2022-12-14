# Generated by Django 4.1.1 on 2022-09-14 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_disciplinehomework_date_disciplinesactual_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinehomework',
            name='actual_file',
            field=models.FileField(blank=True, null=True, upload_to='homework', verbose_name='Дз файл'),
        ),
        migrations.AlterField(
            model_name='disciplinesactual',
            name='actual_file',
            field=models.FileField(blank=True, null=True, upload_to='homework', verbose_name='Дз файл'),
        ),
        migrations.CreateModel(
            name='Uploads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to='homework/%Y/%m/%d', verbose_name='Загруженный файл')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.disciplinehomework', verbose_name='Прикреплён к таблице')),
            ],
            options={
                'verbose_name': 'Загруженный файл',
                'verbose_name_plural': 'Загруженные файлы',
            },
        ),
    ]

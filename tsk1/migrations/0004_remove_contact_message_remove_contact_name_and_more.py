# Generated by Django 4.2.5 on 2023-12-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsk1', '0003_alter_about_image_alter_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.AlterField(
            model_name='creator',
            name='content',
            field=models.TextField(max_length=100),
        ),
    ]

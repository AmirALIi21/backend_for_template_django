# Generated by Django 4.2.5 on 2024-01-02 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsk1', '0005_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tsk1/static/tsk1/img/portfolio/'),
        ),
    ]

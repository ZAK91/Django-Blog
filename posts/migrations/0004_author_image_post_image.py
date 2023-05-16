# Generated by Django 4.2.1 on 2023-05-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(default='', upload_to='authors'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='posts'),
            preserve_default=False,
        ),
    ]

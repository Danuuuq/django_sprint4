# Generated by Django 3.2.16 on 2024-07-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_post_comment_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_photo', verbose_name='Фотография'),
        ),
    ]

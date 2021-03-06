# Generated by Django 3.1.1 on 2021-03-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210314_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post_background_image',
            field=models.ImageField(default='', upload_to='images/background/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

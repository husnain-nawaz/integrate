# Generated by Django 3.1.1 on 2021-03-14 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='post_background_image',
        ),
        migrations.AddField(
            model_name='project',
            name='post_background_image1',
            field=models.ImageField(default='', upload_to='images/project/background/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='post_background_image2',
            field=models.ImageField(default='', upload_to='images/project/background/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='post_background_image3',
            field=models.ImageField(default='', upload_to='images/project/background/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='post_background_image4',
            field=models.ImageField(default='', upload_to='images/project/background/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='post_background_image5',
            field=models.ImageField(default='', upload_to='images/project/background/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='post_catagory_image1',
            field=models.ImageField(default='', upload_to='images/project/catagory/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='post_catagory_image2',
            field=models.ImageField(default='', upload_to='images/project/catagory/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='post_catagory_image3',
            field=models.ImageField(default='', upload_to='images/project/catagory/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='post_image',
            field=models.ImageField(upload_to='images/project/products/'),
        ),
    ]

# Generated by Django 3.1.1 on 2021-03-14 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='project_casual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('post_title', models.CharField(max_length=150)),
                ('post_image', models.ImageField(upload_to='images/project/products/casual/')),
                ('post_main', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='project_formal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('post_title', models.CharField(max_length=150)),
                ('post_image', models.ImageField(upload_to='images/project/products/formal/')),
                ('post_main', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='project_product',
        ),
    ]

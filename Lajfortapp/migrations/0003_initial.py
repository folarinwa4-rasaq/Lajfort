# Generated by Django 5.0.6 on 2024-09-29 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Lajfortapp', '0002_delete_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(max_length=1000000)),
                ('vision', models.TextField(max_length=1000000)),
                ('image', models.ImageField(default='', null=True, upload_to='')),
                ('mission1', models.TextField(max_length=100)),
                ('mission2', models.TextField(max_length=100)),
                ('mission3', models.TextField(max_length=100)),
                ('mission4', models.TextField(max_length=100)),
            ],
        ),
    ]

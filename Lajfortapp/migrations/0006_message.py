# Generated by Django 5.0.6 on 2024-10-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lajfortapp', '0005_gallerie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=1000000)),
            ],
        ),
    ]

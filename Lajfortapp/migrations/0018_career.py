# Generated by Django 5.0.6 on 2024-10-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lajfortapp', '0017_alter_founder_speech_alter_headteacher_speech_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000000, null=True)),
            ],
        ),
    ]
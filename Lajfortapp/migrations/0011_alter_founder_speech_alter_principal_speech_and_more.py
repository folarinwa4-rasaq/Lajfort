# Generated by Django 5.0.6 on 2024-10-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lajfortapp', '0010_alter_founder_speech_alter_principal_speech_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founder',
            name='speech',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='principal',
            name='speech',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='viceprincipal',
            name='speech',
            field=models.TextField(max_length=150),
        ),
    ]

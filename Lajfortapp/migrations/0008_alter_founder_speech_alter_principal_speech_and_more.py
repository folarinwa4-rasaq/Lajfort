# Generated by Django 5.0.6 on 2024-10-01 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lajfortapp', '0007_founder_principal_viceprincipal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founder',
            name='speech',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='principal',
            name='speech',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='viceprincipal',
            name='speech',
            field=models.TextField(max_length=200),
        ),
    ]
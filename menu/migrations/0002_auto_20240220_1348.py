# Generated by Django 3.2.12 on 2024-02-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='description',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='url',
            field=models.CharField(max_length=150),
        ),
    ]

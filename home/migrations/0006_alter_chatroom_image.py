# Generated by Django 5.0 on 2024-01-05 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_chatroom_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='image',
            field=models.ImageField(blank=None, upload_to='static/images'),
        ),
    ]

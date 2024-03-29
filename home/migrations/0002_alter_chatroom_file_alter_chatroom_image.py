# Generated by Django 5.0 on 2024-01-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='file',
            field=models.FileField(blank=None, upload_to='./files/'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='image',
            field=models.ImageField(blank=None, upload_to='./static/'),
        ),
    ]

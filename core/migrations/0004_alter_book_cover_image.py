# Generated by Django 4.1.3 on 2022-11-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_book_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(default='defult.png', upload_to='profile_pics'),
        ),
    ]
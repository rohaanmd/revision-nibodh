# Generated by Django 3.2.7 on 2021-09-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='https://via.placeholder.com/500x500.png?text=Default', upload_to='blog/images'),
        ),
    ]

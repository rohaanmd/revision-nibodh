# Generated by Django 3.2.7 on 2021-09-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='/default/image/default.jpg', upload_to='blog/images'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_viewpost_like_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='logo_img',
            field=models.ImageField(blank=True, default='images/programing.png', null=True, upload_to='images'),
        ),
    ]
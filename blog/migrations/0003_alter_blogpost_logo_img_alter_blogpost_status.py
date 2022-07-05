# Generated by Django 4.0.5 on 2022-06-07 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='logo_img',
            field=models.ImageField(blank=True, default='media/programing.png', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='status',
            field=models.CharField(choices=[('p', 'Published'), ('d', 'Draft')], max_length=10),
        ),
    ]
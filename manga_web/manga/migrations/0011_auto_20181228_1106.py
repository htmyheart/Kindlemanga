# Generated by Django 2.0.8 on 2018-12-28 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0010_auto_20181228_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='image_src',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='manga',
            name='source',
            field=models.TextField(),
        ),
    ]
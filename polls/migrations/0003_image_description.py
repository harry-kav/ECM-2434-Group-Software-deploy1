# Generated by Django 4.0.1 on 2022-02-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
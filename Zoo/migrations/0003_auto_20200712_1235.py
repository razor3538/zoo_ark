# Generated by Django 3.0.8 on 2020-07-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zoo', '0002_auto_20200712_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='marker_B',
        ),
        migrations.AddField(
            model_name='product',
            name='marker_B',
            field=models.ManyToManyField(to='Zoo.NotUnique'),
        ),
    ]
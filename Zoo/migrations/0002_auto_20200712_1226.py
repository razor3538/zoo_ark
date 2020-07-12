# Generated by Django 3.0.8 on 2020-07-12 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Zoo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unique',
            name='name',
            field=models.CharField(choices=[('Animal', 'Animal'), ('Feed', 'Feed'), ('Related Product', 'Related Product')], max_length=50),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('marker_A', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zoo.Unique')),
                ('marker_B', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zoo.NotUnique')),
            ],
        ),
    ]
# Generated by Django 2.2.7 on 2019-12-14 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='good',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='read',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='readtext',
            field=models.CharField(blank=True, default='a', max_length=100, null=True),
        ),
    ]

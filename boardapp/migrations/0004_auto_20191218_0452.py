# Generated by Django 2.2.7 on 2019-12-18 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0003_auto_20191215_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_news_createdby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='newsThumbnail/'),
        ),
    ]
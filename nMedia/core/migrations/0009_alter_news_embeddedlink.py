# Generated by Django 4.0.3 on 2022-04-14 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_news_embeddedlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='embeddedLink',
            field=models.TextField(blank=True, null=True),
        ),
    ]
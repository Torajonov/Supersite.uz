# Generated by Django 3.2.6 on 2021-10-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_blog_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.CharField(max_length=450),
        ),
    ]

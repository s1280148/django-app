# Generated by Django 4.2.3 on 2023-07-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0009_remove_comment_text_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(),
        ),
    ]

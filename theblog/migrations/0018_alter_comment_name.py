# Generated by Django 4.1.3 on 2022-12-17 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0017_remove_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
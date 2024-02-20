# Generated by Django 4.1.3 on 2022-12-15 15:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_post_snippet_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=ckeditor.fields.RichTextField(max_length=255),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-23 03:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
    ]

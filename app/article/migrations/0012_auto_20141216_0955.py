# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import article.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20141216_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thubnail',
            field=models.FileField(upload_to=article.models.get_upload_file_name),
            preserve_default=True,
        ),
    ]

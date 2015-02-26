# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20141216_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thubnail',
            field=models.FileField(default=0, upload_to=''),
            preserve_default=True,
        ),
    ]

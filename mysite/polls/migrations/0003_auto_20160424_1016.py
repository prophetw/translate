# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160424_0949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='poll',
            new_name='question',
        ),
    ]

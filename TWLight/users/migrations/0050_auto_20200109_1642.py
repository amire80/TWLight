# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-09 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0049_auto_20191216_1742")]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="approved_app_reminders",
            field=models.BooleanField(
                default=True,
                help_text="Does this coordinator want approved app reminder notices?",
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="discussion_app_reminders",
            field=models.BooleanField(
                default=True,
                help_text="Does this coordinator want under discussion app reminder notices?",
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="pending_app_reminders",
            field=models.BooleanField(
                default=True,
                help_text="Does this coordinator want pending app reminder notices?",
            ),
        ),
    ]

# Generated by Django 3.1.8 on 2021-05-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0070_remove_userprofile_proxy_notification_sent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="lang",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ar", "العربية"),
                    ("br", "brezhoneg"),
                    ("da", "dansk"),
                    ("de", "Deutsch"),
                    ("en", "English"),
                    ("en-gb", "British English"),
                    ("eo", "Esperanto"),
                    ("es", "español"),
                    ("fa", "فارسی"),
                    ("fi", "suomi"),
                    ("fr", "français"),
                    ("he", "עברית"),
                    ("hi", "हिन्दी"),
                    ("id", "Bahasa Indonesia"),
                    ("ja", "日本語"),
                    ("ko", "한국어"),
                    ("lv", "latviešu"),
                    ("mk", "македонски"),
                    ("mr", "मराठी"),
                    ("my", "မြန်မာဘာသာ"),
                    ("pl", "polski"),
                    ("pt", "português"),
                    ("pt-br", "português do Brasil"),
                    ("ro", "română"),
                    ("ru", "русский"),
                    ("sv", "svenska"),
                    ("ta", "தமிழ்"),
                    ("tr", "Türkçe"),
                    ("uk", "українська"),
                    ("vi", "Tiếng Việt"),
                    ("zh-hans", "中文（简体）"),
                    ("zh-hant", "中文（繁體）"),
                ],
                help_text="Language",
                max_length=128,
                null=True,
            ),
        ),
    ]

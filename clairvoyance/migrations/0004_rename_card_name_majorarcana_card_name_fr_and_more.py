# Generated by Django 4.1.2 on 2022-12-03 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("clairvoyance", "0003_leftdeck_rightdeck"),
    ]

    operations = [
        migrations.RenameField(
            model_name="majorarcana",
            old_name="card_name",
            new_name="card_name_fr",
        ),
        migrations.RenameField(
            model_name="majorarcana",
            old_name="card_signification_gen",
            new_name="card_signification_gen_fr",
        ),
        migrations.RenameField(
            model_name="majorarcana",
            old_name="card_signification_love",
            new_name="card_signification_love_fr",
        ),
        migrations.RenameField(
            model_name="majorarcana",
            old_name="card_signification_warnings",
            new_name="card_signification_warnings_fr",
        ),
        migrations.RenameField(
            model_name="majorarcana",
            old_name="card_signification_work",
            new_name="card_signification_work_fr",
        ),
    ]

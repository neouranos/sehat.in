# Generated by Django 3.2.7 on 2021-09-12 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sehat_in_webproject', '0002_testhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
    ]

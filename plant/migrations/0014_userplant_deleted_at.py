# Generated by Django 5.2.4 on 2025-07-25 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0013_planthistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='userplant',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

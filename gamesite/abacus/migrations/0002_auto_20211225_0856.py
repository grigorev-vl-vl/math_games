# Generated by Django 3.2.9 on 2021-12-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abacus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='answer',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
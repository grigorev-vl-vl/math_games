# Generated by Django 3.2.9 on 2021-12-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abacus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('problems', models.ManyToManyField(to='abacus.Problem')),
            ],
        ),
    ]

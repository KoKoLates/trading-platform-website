# Generated by Django 4.2.1 on 2023-05-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='announcer',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='campaign',
            name='register_num',
            field=models.IntegerField(null=True),
        ),
    ]
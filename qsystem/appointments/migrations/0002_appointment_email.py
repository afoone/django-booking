# Generated by Django 2.1.3 on 2019-02-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default='nada@example.es', max_length=254),
            preserve_default=False,
        ),
    ]
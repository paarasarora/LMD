# Generated by Django 4.1.1 on 2022-09-20 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_members_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.0.7 on 2020-08-23 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_replycomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replycomment',
            name='active',
        ),
    ]
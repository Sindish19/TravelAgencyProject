# Generated by Django 3.0.1 on 2019-12-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DJangoApp', '0002_kontakt_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kontakt',
            name='foto',
        ),
        migrations.AddField(
            model_name='tours',
            name='foto',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
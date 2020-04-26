# Generated by Django 3.0.1 on 2019-12-23 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('pershkrim', models.CharField(max_length=300)),
                ('dataNisjes', models.CharField(max_length=30)),
                ('dataKthimit', models.CharField(max_length=30)),
                ('cmimi', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Kontakt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=1000)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DJangoApp.Tours')),
            ],
        ),
    ]
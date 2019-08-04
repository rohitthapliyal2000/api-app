# Generated by Django 2.2.3 on 2019-07-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=20)),
                ('bank_id', models.IntegerField()),
                ('branch', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=140)),
                ('city', models.CharField(max_length=40)),
                ('district', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=30)),
                ('bank_name', models.CharField(max_length=30)),
            ],
        ),
    ]
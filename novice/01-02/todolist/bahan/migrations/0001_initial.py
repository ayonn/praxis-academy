# Generated by Django 2.2 on 2020-09-09 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bahan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(default='')),
                ('stok', models.IntegerField(default='')),
            ],
        ),
    ]

# Generated by Django 3.2.16 on 2024-03-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0004_congratulation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='Тег')),
            ],
        ),
    ]

# Generated by Django 2.2 on 2019-04-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20190419_0616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, max_length=200, null=True)),
                ('context', models.TextField()),
            ],
        ),
    ]

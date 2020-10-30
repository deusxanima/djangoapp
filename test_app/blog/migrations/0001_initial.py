# Generated by Django 3.1.2 on 2020-10-30 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail_name', models.TextField()),
                ('popularity', models.FloatField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('length', models.FloatField()),
                ('elevation_gain', models.FloatField()),
                ('difficulty', models.IntegerField()),
                ('trail_type', models.CharField(max_length=2)),
                ('area_name', models.CharField(max_length=250)),
                ('city_id', models.IntegerField()),
                ('city_name', models.CharField(max_length=150)),
                ('state_id', models.IntegerField()),
                ('state_name', models.CharField(max_length=50)),
                ('url', models.SlugField(max_length=1000)),
            ],
        ),
    ]
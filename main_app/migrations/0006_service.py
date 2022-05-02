# Generated by Django 4.0.4 on 2022-05-02 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_color_color_patient_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_price', models.IntegerField()),
                ('service_type', models.CharField(max_length=50)),
                ('service_duration', models.DurationField()),
                ('service_description', models.TextField(max_length=200)),
            ],
        ),
    ]
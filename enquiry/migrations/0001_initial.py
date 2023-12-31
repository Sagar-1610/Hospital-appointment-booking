# Generated by Django 4.1.7 on 2023-06-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Visiting_Department', models.CharField(max_length=70)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'), ('Ambiguous', 'Ambiguous')], max_length=20)),
                ('full_name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
                ('aadhar_no', models.IntegerField()),
                ('Country', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('mobile', models.IntegerField()),
                ('email', models.CharField(max_length=80)),
            ],
        ),
    ]

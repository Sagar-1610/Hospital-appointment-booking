# Generated by Django 4.1.7 on 2023-07-14 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='aadhar_no',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
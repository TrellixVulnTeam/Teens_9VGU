# Generated by Django 2.2.3 on 2019-07-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teenager', '0003_remove_student_name_of_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='parent_full_name',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='parent_phone_number',
            field=models.CharField(default=1, max_length=225),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0.2 on 2022-03-15 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PinnocchioConsultingProject', '0002_subjecttype1_subjecttype2_subjecttype3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('colledg_idx', models.IntegerField(primary_key=True, serialize=False)),
                ('colledge_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'colleges',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('department_idx', models.IntegerField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(blank=True, max_length=100, null=True)),
                ('show_as_an_option', models.IntegerField(blank=True, null=True)),
                ('colledg_idx', models.IntegerField()),
            ],
            options={
                'db_table': 'departments',
                'managed': False,
            },
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-01 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0002_creditrequirements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_idx', models.IntegerField()),
                ('subject_name', models.CharField(blank=True, max_length=100, null=True)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('subject_mode', models.CharField(blank=True, max_length=100, null=True)),
                ('subject_code', models.CharField(blank=True, max_length=8, null=True)),
                ('instructor', models.CharField(blank=True, max_length=100, null=True)),
                ('credits', models.IntegerField(blank=True, null=True)),
                ('tags', models.CharField(blank=True, max_length=100, null=True)),
                ('mon', models.CharField(blank=True, max_length=30, null=True)),
                ('tue', models.CharField(blank=True, max_length=30, null=True)),
                ('wed', models.CharField(blank=True, max_length=30, null=True)),
                ('thu', models.CharField(blank=True, max_length=30, null=True)),
                ('fri', models.CharField(blank=True, max_length=30, null=True)),
                ('sat', models.CharField(blank=True, max_length=30, null=True)),
                ('sun', models.CharField(blank=True, max_length=30, null=True)),
                ('x_grade', models.IntegerField(blank=True, null=True)),
                ('o_grade', models.IntegerField(blank=True, null=True)),
                ('x_department', models.IntegerField(blank=True, null=True)),
                ('o_department', models.IntegerField(blank=True, null=True)),
                ('subject_type_1_idx', models.IntegerField()),
                ('subject_type_1_name', models.CharField(blank=True, max_length=100, null=True)),
                ('subject_type_2_idx', models.IntegerField()),
                ('subject_type_2_name', models.CharField(blank=True, max_length=100, null=True)),
                ('subject_type_3_idx', models.IntegerField()),
                ('subject_type_3_name', models.CharField(blank=True, max_length=100, null=True)),
                ('department_idx', models.IntegerField()),
                ('department_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'subjects',
                'managed': False,
            },
        ),
    ]

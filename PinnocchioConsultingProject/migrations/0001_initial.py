# Generated by Django 4.0.2 on 2022-03-15 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CreditRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_option_idx', models.IntegerField()),
                ('started_year', models.IntegerField(blank=True, null=True)),
                ('ended_year', models.IntegerField(blank=True, null=True)),
                ('basic_subject', models.IntegerField(blank=True, null=True)),
                ('necess_subject', models.IntegerField(blank=True, null=True)),
                ('major_total_subject', models.IntegerField(blank=True, null=True)),
                ('common_subject', models.IntegerField(blank=True, null=True)),
                ('key_subject', models.IntegerField(blank=True, null=True)),
                ('total_subjects', models.IntegerField(blank=True, null=True)),
                ('department_idx', models.IntegerField()),
                ('major_idx', models.IntegerField()),
                ('track_idx', models.IntegerField()),
                ('entry_route_idx', models.IntegerField()),
            ],
            options={
                'db_table': 'credit_requirements',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MicroCases',
            fields=[
                ('special_option_idx', models.IntegerField(primary_key=True, serialize=False)),
                ('hashed_options', models.CharField(blank=True, max_length=40, null=True)),
                ('entry_year', models.IntegerField(blank=True, null=True)),
                ('basic_major_subject', models.IntegerField(blank=True, null=True)),
                ('necess_major_subject', models.IntegerField(blank=True, null=True)),
                ('total_major_subject', models.IntegerField(blank=True, null=True)),
                ('common_GE_subject', models.IntegerField(blank=True, null=True)),
                ('core_GE_subject', models.IntegerField(blank=True, null=True)),
                ('total_subjects', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'micro_cases',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('subject_idx', models.IntegerField(primary_key=True, serialize=False)),
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
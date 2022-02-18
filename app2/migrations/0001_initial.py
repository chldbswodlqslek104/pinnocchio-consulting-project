# Generated by Django 4.0.2 on 2022-02-17 23:45

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
            name='Classes',
            fields=[
                ('idx', models.IntegerField(primary_key=True, serialize=False)),
                ('교과명', models.CharField(blank=True, max_length=8, null=True)),
                ('학부_학과', models.CharField(blank=True, db_column='학부/학과', max_length=6, null=True)),
                ('트랙', models.CharField(blank=True, max_length=5, null=True)),
                ('전공', models.CharField(blank=True, max_length=45, null=True)),
                ('시간대', models.CharField(blank=True, max_length=5, null=True)),
                ('전공기초', models.CharField(blank=True, max_length=2, null=True)),
                ('전공필수', models.CharField(blank=True, max_length=2, null=True)),
                ('필수교양', models.CharField(blank=True, max_length=2, null=True)),
                ('핵심교양', models.CharField(blank=True, max_length=2, null=True)),
                ('mach교양', models.CharField(blank=True, db_column='MACH교양', max_length=2, null=True)),
                ('mach실습', models.CharField(blank=True, db_column='MACH실습', max_length=2, null=True)),
            ],
            options={
                'db_table': 'classes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CreditRequirements',
            fields=[
                ('case', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('subcase', models.CharField(blank=True, max_length=10, null=True)),
                ('start', models.IntegerField(blank=True, null=True)),
                ('startsemester', models.IntegerField(blank=True, null=True)),
                ('finish', models.IntegerField(blank=True, null=True)),
                ('finishsemster', models.IntegerField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
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
            name='OtherRequirements',
            fields=[
                ('case', models.CharField(max_length=22, primary_key=True, serialize=False)),
                ('subcase2', models.CharField(blank=True, max_length=10, null=True)),
                ('start', models.IntegerField(blank=True, null=True)),
                ('startsemester', models.IntegerField(blank=True, null=True)),
                ('finish', models.IntegerField(blank=True, null=True)),
                ('finishsemester', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'other_requirements',
                'managed': False,
            },
        ),
    ]

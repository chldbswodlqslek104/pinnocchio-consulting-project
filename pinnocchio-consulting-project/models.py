from django.db import models

# Create your models here.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)
    
    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
    
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    
    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    
    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
    
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
        

class CreditRequirements(models.Model):
    special_option_idx = models.IntegerField()
    started_year = models.IntegerField(blank=True, null=True)
    ended_year = models.IntegerField(blank=True, null=True)
    basic_subject = models.IntegerField(blank=True, null=True)
    necess_subject = models.IntegerField(blank=True, null=True)
    major_total_subject = models.IntegerField(blank=True, null=True)
    common_subject = models.IntegerField(blank=True, null=True)
    key_subject = models.IntegerField(blank=True, null=True)
    total_subjects = models.IntegerField(blank=True, null=True)
    department_idx = models.IntegerField()
    major_idx = models.IntegerField()
    track_idx = models.IntegerField()
    entry_route_idx = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'credit_requirements'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        
        
class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MicroCases(models.Model):
    special_option_idx = models.IntegerField(primary_key=True)
    hased_options = models.CharField(max_length=40, blank=True, null=True)
    entry_year = models.IntegerField(blank=True, null=True)
    basic_subject = models.IntegerField(blank=True, null=True)
    necess_subject = models.IntegerField(blank=True, null=True)
    major_total_subject = models.IntegerField(blank=True, null=True)
    common_subject = models.IntegerField(blank=True, null=True)
    key_subject = models.IntegerField(blank=True, null=True)
    total_subjects = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'micro_cases'


class Subjects(models.Model):
    subject_idx = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=100, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    subject_mode = models.CharField(max_length=100, blank=True, null=True)
    subject_code = models.CharField(max_length=8, blank=True, null=True)
    instructor = models.CharField(max_length=100, blank=True, null=True)
    credits = models.IntegerField(blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True, null=True)
    mon = models.CharField(max_length=30, blank=True, null=True)
    tue = models.CharField(max_length=30, blank=True, null=True)
    wed = models.CharField(max_length=30, blank=True, null=True)
    thu = models.CharField(max_length=30, blank=True, null=True)
    fri = models.CharField(max_length=30, blank=True, null=True)
    sat = models.CharField(max_length=30, blank=True, null=True)
    sun = models.CharField(max_length=30, blank=True, null=True)
    x_grade = models.IntegerField(blank=True, null=True)
    o_grade = models.IntegerField(blank=True, null=True)
    x_department = models.IntegerField(blank=True, null=True)
    o_department = models.IntegerField(blank=True, null=True)
    subject_type_1_idx = models.IntegerField()
    subject_type_1_name = models.CharField(max_length=100, blank=True, null=True)
    subject_type_2_idx = models.IntegerField()
    subject_type_2_name = models.CharField(max_length=100, blank=True, null=True)
    subject_type_3_idx = models.IntegerField()
    subject_type_3_name = models.CharField(max_length=100, blank=True, null=True)
    department_idx = models.IntegerField()
    department_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subjects'



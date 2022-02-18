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


class Classes(models.Model):
    idx = models.IntegerField(primary_key=True)
    교과명 = models.CharField(max_length=8, blank=True, null=True)
    학부_학과 = models.CharField(db_column='학부/학과', max_length=6, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    트랙 = models.CharField(max_length=5, blank=True, null=True)
    전공 = models.CharField(max_length=45, blank=True, null=True)
    시간대 = models.CharField(max_length=5, blank=True, null=True)
    전공기초 = models.CharField(max_length=2, blank=True, null=True)
    전공필수 = models.CharField(max_length=2, blank=True, null=True)
    필수교양 = models.CharField(max_length=2, blank=True, null=True)
    핵심교양 = models.CharField(max_length=2, blank=True, null=True)
    mach교양 = models.CharField(db_column='MACH교양', max_length=2, blank=True, null=True)  # Field name made lowercase.
    mach실습 = models.CharField(db_column='MACH실습', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classes'


class CreditRequirements(models.Model):
    case = models.CharField(primary_key=True, max_length=22)
    subcase = models.CharField(max_length=10, blank=True, null=True)
    start = models.IntegerField(blank=True, null=True)
    startsemester = models.IntegerField(blank=True, null=True)
    finish = models.IntegerField(blank=True, null=True)
    finishsemster = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

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


class OtherRequirements(models.Model):
    case = models.CharField(primary_key=True, max_length=22)
    subcase2 = models.CharField(max_length=10, blank=True, null=True)
    start = models.IntegerField(blank=True, null=True)
    startsemester = models.IntegerField(blank=True, null=True)
    finish = models.IntegerField(blank=True, null=True)
    finishsemester = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_requirements'
from django.db import models

# Create your models here.

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



from django.db import models

# Create your models here.
class Requirements(models.Model):
    #졸업 요건 모델
    special_option_idx = models.IntegerField()
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
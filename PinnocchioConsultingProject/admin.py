from django.contrib import admin
from .models import MicroCases, Subjects
# Register your models here.

# class MicroCasesAdmin(admin.ModelAdmin):
#     list_display = ('special_option_idx', 'hased_options', 'entry_year', 'basic_subject',
#     'necess_subject', 'major_total_subject', 'common_subject', 'key_subject','total_subjects')

admin.site.register(MicroCases)

class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('subject_idx', 'subject_name', 'grade', 'subject_mode', 'subject_code', 'instructor',
    'credits', 'tags', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'x_grade', 'o_grade', 
    'x_department', 'o_department', 'subject_type_1_idx', 'subject_type_1_name', 'subject_type_2_idx', 
    'subject_type_2_name', 'subject_type_3_idx', 'subject_type_3_name', 'department_idx', 
    'department_name')

admin.site.register(Subjects, SubjectsAdmin)

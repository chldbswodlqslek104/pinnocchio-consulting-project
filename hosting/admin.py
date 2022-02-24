from django.contrib import admin
from .models import MicroCases
# Register your models here.

class MicroCasesAdmin(admin.ModelAdmin):
    list_display = ('special_option_idx', 'hased_options', 'entry_year', 'basic_subject',
    'necess_subject', 'major_total_subject', 'common_subject', 'key_subject','total_subjects')

admin.site.register(MicroCases, MicroCasesAdmin)

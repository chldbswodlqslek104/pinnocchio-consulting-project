from rest_framework import serializers
from  .models import Subjects, MicroCases

class SubjectsSerializer(serializers.ModelSerializer):
     class Meta:
        model = Subjects
        fields = '__all__'

class MicroCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroCases
        fields = [
            "special_option_idx",
            "hashed_options",
            "entry_year",
            "basic_major_subject",
            "necess_major_subject",
            "total_major_subject",
            "common_GE_subject",
            "core_GE_subject",
            "total_subjects",
        ]


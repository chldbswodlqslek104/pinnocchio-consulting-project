#serializers.py
from rest_framework import serializers
from .models import Requirements

class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = [
                'special_option_idx',
                'hased_options',
                'entry_year',
                'basic_subject',
                'necess_subject',
                'major_total_subject',
                'common_subject',
                'key_subject',
                'total_subjects'
                ]

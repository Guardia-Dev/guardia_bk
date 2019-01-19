from sepicat.data_models.year_analysis import YearAnalysis

from rest_framework import serializers


class YearAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearAnalysis
        fields = (
            'login',
            'year',
            'repo_actions',
        )

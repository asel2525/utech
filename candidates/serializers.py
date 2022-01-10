from rest_framework import serializers

from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = ['id', 'voter', 'surname', 'name', 'information', 'point']
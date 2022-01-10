from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Candidate
from .serializers import CandidateSerializer

class CandidateViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes=[IsAuthenticated, ]

    @action(methods=['put', 'patch', ], detail=True)
    def vote(self, request, *args, **kwargs):
        candidate = self.get_object()
        candidate.point+=1
        candidate.save()
        return Response({'success': True})


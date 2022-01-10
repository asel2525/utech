from rest_framework.routers import SimpleRouter

from .views import CandidateViewSet

router = SimpleRouter()

router.register('candidates', CandidateViewSet)

urlpatterns = []

urlpatterns += router.urls
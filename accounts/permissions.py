from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib.auth import get_user_model
from candidate.models import Candidate


User = get_user_model()


class DiversePermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        ru = request.user
        if request.method in SAFE_METHODS:
            return True
        elif ru.user_type == User.UserType.ADMIN:
            return True
        elif ru.user_type == User.UserType.VOTER:
            if ru == obj.voter:
                return True
        else:
            return False
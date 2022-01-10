from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Candidate(models.Model):
	voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candidates')
	surname = models.CharField(max_length=80)
	name = models.CharField(max_length=50)
	information = models.CharField(max_length=300)
	point = models.IntegerField(default=0)

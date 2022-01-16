from rest_framework import serializers

from .models import *


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'company_name', 'city', 'state', 'zip', 'email', 'web', 'age']

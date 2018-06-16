from .models import *
import django_filters

class UserFilter(django_filters.FilterSet):
	class Meta:
		model = Profile
		fields = {'user__username' : ['icontains'],
				  'user__first_name' : ['icontains'],
				  'user__email' : ['icontains'],
			      'tipo' : ['icontains'],
		}

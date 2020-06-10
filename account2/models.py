from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Contact(models.Model):
	user_from = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='from_set')
	user_to = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='to_set')
	created = models.DateTimeField(auto_now_add=True, db_index=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return '{} 跟隨 (關注) {}'.format(self.user_from, self.user_to)



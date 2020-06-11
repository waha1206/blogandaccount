from django.db import models
from django.contrib.auth.models import User

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


# 增加一個字段
# 'self' 可以用 to=User 取代
# through 意思是與哪個 class 產生關聯  例如 througth=Contact
# synnetrical=多對多之間的關係不一定是對等的(非對稱關係)，你關聯我，但是我並不一定要關聯你，這裡指的是 User 與 Contact之間的關係
# 非數據庫裡的字段
User.add_to_class('following', models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))

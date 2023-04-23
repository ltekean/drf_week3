from django.db import models
from users.models import User
from django.urls import reverse
# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 1대 다수
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='%Y/%m')
    # upload_to에 따라 media 폴더 안에 날짜에 맞는 폴더가 따로 생긴다.
    # m은 month, M은 minute이니 주의할 것
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'article_id': self.id})
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
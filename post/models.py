from django.db import models
from django.utils import timezone
from user.models import User
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Пользователь')
    title = models.CharField(max_length=128,verbose_name="Заголовок поста")
    content = models.TextField(verbose_name="Контент поста")
    time_stamp = models.DateTimeField(default=timezone.now, verbose_name="Время создания поста")
    edited = models.BooleanField(default=False,verbose_name="Редактирован")
 
    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'

    def __str__(self):
        return f'{self.title}: {self.time_stamp} ({self.edited})'
    
class PostAttachment(models.Model):
    name = models.CharField(verbose_name='Название файла',blank=True)
    file = models.FileField(upload_to='images/',verbose_name="Файл")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,verbose_name="Пост")

    def save(self, *args, **kwargs):
        file_name=self.file.name.split('.')[0].capitalize
        self.name=file_name
        super().save(*args, **kwargs)

    class Meta:
        verbose_name='Файл'
        verbose_name_plural='Файлы'

    def __str__(self):
        return f'{self.file}:{self.post}'
    
#Comment = модель
# author = автор
# content = комм
# post = пост как файл
# time = время публикации комм timestamp из модели пост

class Comment(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    content = models.TextField(verbose_name="контент комментария")
    post = models.ForeignKey(Post,on_delete=models.CASCADE, verbose_name='пост')
    time_stamp  = models.DateTimeField(default=timezone.now, verbose_name="Время публикации комментария")
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    
    def __str__(self):
        return f'{self.author}:{self.post.title}:{self.time_stamp}'
    

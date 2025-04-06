from django.contrib import admin
from .models import Post,PostAttachment,Comment
# Register your models here.

@admin.register(Post)
class CustomPostAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Автор', {'fields': ('author',)}),
        ('Информация поста (Русский)', {'fields': ('title', 'content',)}),
        ('Доп.инфо', {'fields': ('time_stamp', 'edited',)}),
    )
    add_fieldsets = (
        ('Автор', {'fields': ('author',)}),
        ('Информация поста (Русский)', {'fields': ('title', 'content',)}),
    )
    list_display = ('author', 'title', 'content', 'time_stamp','edited')
    search_fields=('title','content')
    ordering = ('-time_stamp',)
    def get_fieldsets(self, request, obj = None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets
@admin.register(Comment)
class CustomCommentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Автор',{'fields':('author',)}),
        ('Информация о комментарии',{'fields':('content','post',)}),
        ('Доп.инфо',{'fields':('time_stamp',)}),
    )
    add_fieldsets = (
        ('Автор', {'fields': ('author',)}),
        ('Информация о комментарии', {'fields': ('content', 'post',)}),
    )
    def get_fieldsets(self, request, obj = None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets

@admin.register(PostAttachment)
class CustomPostAttachmentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Файлы для поста', {"fields": ('name','file',)}), 
        ('Пост', {"fields": ('post',)})
    )
    add_fieldsets = (
        ('Файлы для поста', {"fields": ('file',)}), 
        ('Пост', {"fields": ('post',)})
    )
    list_display = ('name','file', 'post')
    search_fields = ('post__title',)
    ordering = ('post',)
    
    def get_fieldsets(self, request, obj = None):
        if obj:
            return self.fieldsets
        return self.add_fieldsets

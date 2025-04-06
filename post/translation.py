from modeltranslation.translator import register, TranslationOptions
from .models import Post

@register(Post)
class PostTranslation(TranslationOptions):
    fields = ('title', 'content')
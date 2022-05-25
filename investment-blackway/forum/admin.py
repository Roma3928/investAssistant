from django.contrib import admin
from .models import Tag, LikeDislike, Question, Answer

admin.site.register(Tag)
admin.site.register(LikeDislike)
admin.site.register(Question)
admin.site.register(Answer)

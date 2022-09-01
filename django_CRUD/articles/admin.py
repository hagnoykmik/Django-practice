from django.contrib import admin
from .models import Article

# Register your models here.
# 관리자 페이지에 등록
admin.site.register(Article)
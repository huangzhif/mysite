#coding:utf-8
from django.contrib import admin
from .models import BlogArticles


class BlogArticlesAdmin(admin.ModelAdmin):
	list_display = ("title","author","publish") #字段显示信息
	list_filter = ("publish","author") #过滤条件：日期和作者
	search_fields = ("title","body") #查询条件：文章名与文章内容
	#raw_id_fields = ("author",) #编辑文章时，作者显示其ID
	date_hierarchy = "publish" #在页面增加日期的分层导航功能
	ordering = ['-publish','author']


admin.site.register(BlogArticles,BlogArticlesAdmin)

# Register your models here.


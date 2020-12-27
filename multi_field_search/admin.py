from django.contrib import admin

# Register your models here.
from multi_field_search.models import Lesson, Post, Profile

admin.site.register([Lesson, Post, Profile])
